<template>
  <main class="container mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
    <section class="lg:col-span-2">
        <h2 class="text-3xl font-bold mb-6">Últimas notícias</h2>
        <ContentList path="/posts" v-slot="{ list }">
        <div class="posts-list">
            <div
            v-for="post in sortedPosts(list).slice(0, displayCount)"
            :key="post._path"
            class="blog-card rounded-2xl overflow-hidden mb-6 transition-transform transform hover:scale-100"
            >
            <NuxtLink :to="post.slug" class="block w-full h-full">
                <div class="h-[200px] sm:h-[300px] relative">
                <img
                    v-if="post.thumbnail"
                    :src="post.thumbnail"
                    :alt="post.title"
                    class="absolute w-full h-full object-cover"
                />
                </div>
    
                <div class="blog-card--meta absolute bottom-0 w-full bg-gradient-to-t from-black to-transparent text-white p-3 sm:p-4">
                <h3 class="text-lg sm:text-2xl font-bold text-shadow-lg">{{ post.title }}</h3>
                <div class="text-xs sm:text-sm text-gray-300">{{ post.date.split(' ')[0] }}</div>
                <div v-if="post.tags" class="mt-2 text-xs flex flex-wrap gap-1 sm:space-x-2">
                    <span
                    v-for="tag in post.tags.slice(0, 3)"
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
    </section>
    <aside class="lg:col-span-1">
        <Stripe />
    </aside>
  </main>
</template>

<script lang="ts" setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import type { ParsedContent } from '@nuxt/content'

// Sem login necessário para a página
definePageMeta({ auth: false });

const displayCount = ref(10)
const loading = ref(false)

function sortedPosts(list: ParsedContent[]) {
  return list.slice().sort((a: ParsedContent, b: ParsedContent) => {
    const dateA = parseDate(a.date);
    const dateB = parseDate(b.date);
    return dateB.getTime() - dateA.getTime(); // dateB - dateA para mostrar mais recente primeiro
  });
}

function parseDate(dateStr: string): Date {
  const [day, month, yearAndTime] = dateStr.split('/');
  const [year, time] = yearAndTime.split(' ');
  return new Date(`${year}-${month}-${day}T${time}`);
}

function handleScroll() {
  const bottomOfWindow = window.innerHeight + window.scrollY >= document.documentElement.offsetHeight - 10;
  if (bottomOfWindow && !loading.value) {
    loading.value = true;
    setTimeout(() => {
      displayCount.value += 10;
      loading.value = false;
    }, 500);
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
})
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
