import Aura from "@primevue/themes/aura";

export default defineNuxtConfig({
  app: {
       head: {
         title: 'Eletrificado - Notícias sobre Carros Elétricos',
          meta: [
            // Open Graph Meta Tags (para Facebook, LinkedIn, etc.)
            { property: 'og:title', content: 'Eletrificado - Notícias sobre Carros Elétricos' },
            { property: 'og:description', content: 'Fique por dentro das últimas notícias sobre carros elétricos.' },
            { property: 'og:image', content: '/path-to-image.jpg' }, // Imagem para preview
            { property: 'og:url', content: 'https://seusite.com' },
            { property: 'og:type', content: 'website' },
    
            // Twitter Card Meta Tags
            { name: 'twitter:card', content: 'summary_large_image' },
            { name: 'twitter:title', content: 'Eletrificado - Notícias sobre Carros Elétricos' },
            { name: 'twitter:description', content: 'Fique atualizado sobre os carros elétricos.' },
            { name: 'twitter:image', content: '/path-to-image.jpg' }, // Imagem para Twitter Card
          ],
          link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
       }
   },

		compatibilityDate: "2024-08-09",

		typescript: {
						typeCheck: true,
		},

		devtools: {
						enabled: true,
		},

		modules: [
		 "@nuxt/content",
		 "@nuxt/image",
		 "@nuxtjs/tailwindcss",
		 "@primevue/nuxt-module",
		 "@sidebase/nuxt-auth",
		 "nuxt-posthog",
		 'nuxt-gtag',
		],
		
		content: {
		experimental: {
      search: {}
		}
  },

		// https://tailwind.primevue.org/nuxt/
		// https://github.com/primefaces/primevue-examples/blob/main/nuxt-styled-tailwind/nuxt.config.ts
		primevue: {
						options: {
										theme: {
														preset: Aura,
										},
						},
		},

		// Files added here are included in all pages. We want to add the PrimeIcons
		// CSS
		//
		// https://nuxt.com/docs/api/nuxt-config#css
		// https://github.com/primefaces/primeicons
		// https://primevue.org/icons/
		css: ["primeicons/primeicons.css"],

		auth: {
						// This makes all pages private by default. If you want to make a page
						// public, you can use `definePageMeta({ auth: false })` on the page `setup`
						//
						// https://auth.sidebase.io/guide/application-side/configuration#globalappmiddleware
						globalAppMiddleware: true,

						// https://auth.sidebase.io/guide/authjs/quick-start#configuration
						provider: {
										type: "authjs",
										trustHost: false,
										defaultProvider: "auth0",
										addDefaultCallbackUrl: "/",
						},
		},
		
		gtag: {
      id: process.env.NUXT_GTAG_ID,
    },

		// Configurations from here should be overriden by using `.env` or environment
		// variables. Check `.env.example` for documentation on each of those values
		//
		// https://nuxt.com/docs/guide/going-further/runtime-config
		runtimeConfig: {
						secret: "",

						authOrigin: "",

						auth0: {
										issuer: "",
										clientId: "",
										clientSecret: "",
						},
						
						stripe: {
						secretKey: "",
						successUrl: "",
		},

						// Configurations inside the `public` object are available to the client.
						// Eg. in the browser
						public: {
										posthog: {
												host: process.env.NUXT_POSTHOG_HOST,
    publicKey: process.env.NUXT_POSTHOG_PUBLIC_KEY,
										},
						},
		},
});