<template>
  <aside class="hidden lg:block bg-gray-800 text-white p-6 rounded-xl shadow-2xl">
    <h2 class="text-2xl font-bold mb-4">Apoie o Projeto</h2>
    <p class="mb-6">
      Se você gosta de carros elétricos e o nosso conteúdo é útil para você, considere fazer uma doação!
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

    <p v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</p>
  </aside>
  
  <aside class="fixed bottom-4 right-4 lg:hidden">
    <button v-if="!isExpanded" @click="isExpanded = true" class="text-white bg-blue-500 px-6 py-3 rounded-full text-2xl hover:bg-blue-600 shadow-lg">
      💸 Apoiar
    </button>
    
    <button 
        v-else 
        @click="isExpanded = false" 
        class="absolute top-3 right-3 text-white bg-transparent px-4 py-2 text-lg flex items-center justify-center w-8 h-8"
      >
      <i class="pi pi-times text-white text-xl"></i>
    </button>
  
    <div v-if="isExpanded" class="bg-gray-800 text-white p-4 rounded-xl shadow-2xl mt-2">
        <h2 class="text-xl font-bold mb-2">Apoie o Projeto</h2>
        <p class="text-sm mb-2">Considere fazer uma doação para o site!</p>
        
        <div class="mb-6">
            <button
            v-for="preset in presets"
            :key="preset"
            @click="selectAmount(preset)"
            :class="['px-3 py-2 rounded-full mr-2', { 'bg-blue-600': amount === preset, 'bg-gray-600': amount !== preset }]"
            class="text-white hover:bg-blue-500 transition-colors"
            >
            R$ {{ preset / 100 }}
            </button>
        </div>
    <div class="text-right">
        <button
            @click="generatePaymentLink"
            class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition-colors"
            >
            Quero ajudar!
        </button>
    </div>
        <p v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</p>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isExpanded = ref(false);

const amount = ref<number | null>(null)
const errorMessage = ref<string | null>(null)
const presets = [500, 1000, 5000, 10000]

const selectAmount = (preset: number) => {
  amount.value = preset
  errorMessage.value = null
}

const generatePaymentLink = async () => {
  const selectedAmount = amount.value

  if (!selectedAmount) {
    errorMessage.value = 'Por favor, selecione um valor válido.'
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

<style>
.fixed {
  position: fixed;
}

.bottom-4 {
  bottom: 1rem;
}

.right-4 {
  right: 1rem;
}

.rounded-full {
  border-radius: 9999px;
}

.shadow-lg {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>