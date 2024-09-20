<template>
  <ClientOnly>
    <Posthog />
  </ClientOnly>

  <main class="bg-gray-800 text-white">
    <header class=" flex justify-between items-end m-4">
        <div class="flex items-center">
            <img src="/img/favicon.png" alt="Eletrificado Logo" class="h-12 w-12 mr-2" />
            <div>
            <h1 class="text-2xl font-semibold">
                <NuxtLink to="/">Eletrificado</NuxtLink>
            </h1>
            <p class="text-gray-500">Notícias sobre o mundo dos carros elétricos</p>
            </div>
        </div>
    </header>
    <Navbar class="m-4" />
    <div class="container mx-auto p-6">
      <NuxtPage class="m-4" />
    </div>
    <footer class="p-4 bg-gray-900 text-white text-center">
      <p>&copy; 2024 Eletrificado. All rights reserved.</p>
    </footer>
  </main>
</template>