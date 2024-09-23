<template>
  <ClientOnly>
    <Posthog />
  </ClientOnly>

  <main class="bg-gray-800 text-white min-h-screen flex flex-col">
    <header class="bg-gray-900 flex justify-between items-center p-4 relative">
      <div class="flex items-center">
        <img src="/img/favicon.png" alt="Eletrificado Logo" class="h-12 w-12 mr-2" />
        <div>
          <h1 class="text-2xl font-semibold">
            <NuxtLink to="/">Eletrificado</NuxtLink>
          </h1>
          <p class="text-gray-500">Notícias sobre o mundo dos carros elétricos</p>
        </div>
      </div>

      <!-- Navbar -->
      <div class="absolute right-0 flex items-center">
        <Navbar class="transparent-navbar" />
      </div>
    </header>

    <div class="container mx-auto p-6">
      <NuxtPage class="m-4" />
    </div>

    <footer class="p-4 bg-gray-900 text-white text-center">
      <p>&copy; 2024 Eletrificado. All rights reserved.</p>
    </footer>
  </main>
</template>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 100% da altura da viewport */
}

.header {
  background-color: #1a202c; /* Uma cor diferente, mas ainda similar ao estilo geral */
}

.transparent-navbar {
  background-color: transparent; /* Torna a navbar transparente */
}

.navbar a {
  color: white;
  text-decoration: none;
}

.navbar a:hover {
  text-decoration: underline;
}

.container {
  flex-grow: 1; /* Faz o conteúdo crescer e ocupar o espaço disponível */
}
</style>