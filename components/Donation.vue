<template>
  <aside class="bg-gray-800 text-white p-6 rounded-xl shadow-2xl">
    <h2 class="text-2xl font-bold mb-4">Apoie o Projeto</h2>
    <p class="mb-6">
      Se você gosta de carros elétricos e o nosso conteúdo é útil para você, considere fazer uma doação
      para continuarmos expandindo o site com conteúdos de qualidade ainda melhor!
    </p>

    <div class="mb-6">
      <button
        v-for="preset in presets"
        :key="preset"
        @click="selectAmount(preset)"
        :class="['px-4 py-2 rounded-full mr-2', { 'bg-blue-600': amount === preset, 'bg-gray-600': amount !== preset }]"
        class="text-white hover:bg-blue-500 transition-colors"
      >
        R$ {{ preset / 100 }}
      </button>
    </div>

    <button
      @click="generatePaymentLink"
      class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition-colors"
    >
      Quero ajudar!
    </button>

    <!-- Aviso de erro -->
    <p v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</p>
  </aside>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const amount = ref<number | null>(null)
const customAmount = ref<number | null>(null)
const errorMessage = ref<string | null>(null)
const presets = [500, 1000, 5000, 10000]

const selectAmount = (preset: number) => {
  amount.value = preset
  customAmount.value = null
  errorMessage.value = null
}

const generatePaymentLink = async () => {
  const selectedAmount = customAmount.value ? customAmount.value * 100 : amount.value

  if (!selectedAmount || selectedAmount <= 0) {
    errorMessage.value = 'Por favor, insira ou selecione um valor válido.'
    return
  }

  errorMessage.value = null

  try {
    const response = await fetch('/api/donation', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ amount: selectedAmount })
    })

    const { url } = await response.json()

    window.location.href = url
  } catch (error) {
    console.error('Erro ao criar o link de pagamento:', error)
  }
}
</script>