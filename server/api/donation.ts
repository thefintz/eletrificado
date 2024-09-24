import Stripe from 'stripe'
import { H3Event, readBody } from 'h3'

export default defineEventHandler(async (event: H3Event) => {
  const stripe = new Stripe(process.env.NUXT_STRIPE_SECRET_KEY as string)

  const body = await readBody(event)
  const { amount } = body

  if (!amount || amount <= 0) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Valor inválido para a doação.'
    })
  }

  const session = await stripe.checkout.sessions.create({
    line_items: [{
      price_data: {
        currency: 'brl',
        product_data: {
          name: 'Doação para o Eletrificado',
        },
        unit_amount: amount,
      },
      quantity: 1,
    }],
    mode: 'payment',
    success_url: process.env.NUXT_STRIPE_SUCCESS_URL,
  })

  return { url: session.url }
})