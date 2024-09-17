<template>
  <main>
    <ContentList path="/posts" v-slot="{ list }">
      <div
        v-for="post in list"
        :key="post._path"
        class="blog-card rounded-2xl overflow-hidden mb-6 transition-transform transform hover:scale-105"
      >
        <NuxtLink :to="post.slug" class="block w-full h-full">
          <div class="h-[300px] relative">
            <img
              v-if="post.thumbnail"
              :src="post.thumbnail"
              :alt="post.title"
              class="absolute w-full h-full object-cover"
            />
          </div>

          <div class="blog-card--meta absolute bottom-0 w-full bg-gradient-to-t from-black to-transparent text-white p-4">
            <h3 class="text-2xl font-bold">{{ post.title }}</h3>
            <div class="text-sm text-gray-300">{{ post.date }}</div>
            <div v-if="post.tags" class="mt-2 text-xs flex space-x-2">
              <span
                v-for="tag in post.tags"
                :key="tag"
                class="bg-gray-800 bg-opacity-75 px-2 py-1 rounded-full"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </NuxtLink>
      </div>
    </ContentList>
  </main>
</template>

<script lang="ts">
</script>

<style scoped>
.blog-card {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Sombra suave */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Suaviza a transformação e sombra */
}

.blog-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Sombra mais forte no hover */
}
</style>
