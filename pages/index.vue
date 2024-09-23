<template>
  <main class="container mx-auto px-4 py-8">
    <h2 class="text-3xl font-bold mb-6">Últimas notícias</h2>
    <ContentList path="/posts" v-slot="{ list }">
      <div class="posts-list">
        <div
          v-for="post in sortedPosts(list)"
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
              <h3 class="text-2xl font-bold text-shadow-lg">{{ post.title }}</h3>
              <div class="text-sm text-gray-300">{{ post.date.split(' ')[0] }}</div>
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
      </div>
    </ContentList>
  </main>
</template>

<script lang="ts" setup>
import type { ParsedContent } from '@nuxt/content'

definePageMeta({ auth: false });

// Função para ordenar os posts pela data
function sortedPosts(list: ParsedContent[]) {
  return list.slice().sort((a: ParsedContent, b: ParsedContent) => {
    const dateA = parseDate(a.date);
    const dateB = parseDate(b.date);
    return dateB.getTime() - dateA.getTime(); // dateB - dateA para mostrar mais recente primeiro
  });
}

// Função para converter a data no formato "DD/MM/AAAA HH:MM" em um objeto Date
function parseDate(dateStr: string): Date {
  const [day, month, yearAndTime] = dateStr.split('/');
  const [year, time] = yearAndTime.split(' ');
  return new Date(`${year}-${month}-${day}T${time}`);
}
</script>

<style scoped>
.posts-list {
  max-width: 900px;
  margin-left: 0;
  margin-right: auto;
}

.blog-card {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.blog-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.text-shadow-lg {
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}

.blog-card--meta {
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.95) 20%, rgba(0, 0, 0, 0.75) 50%, rgba(0, 0, 0, 0.6) 75%, rgba(0, 0, 0, 0) 100%);
}
</style>
