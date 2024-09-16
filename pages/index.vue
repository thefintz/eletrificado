<template>
    <main>
        <ContentList path="/posts" v-slot="{ list }">
        <div
                v-for="post in list"
                :key="post._path"
                class="blog-card rounded-2xl overflow-hidden mb-4"
              >
                <div class="h-[300px] relative">
                  <img
                    v-if="post.thumbnail"
                    :src="post.thumbnail"
                    :alt="post.title"
                    class="absolute w-full h-full object-cover"
                  />
                </div>
        
                <div class="blog-card--meta my-4 ml-4">
                  <h3 class="text-2xl font-bold">
                    <NuxtLink :to="post.slug">{{ post.title }}</NuxtLink>
                  </h3>
                  <div class="text-sm text-gray-500 mt-px block">{{ post.date }}</div>
                  <div v-if="post.tags" class="mt-2 text-xs">
                    <span v-for="tag in post.tags" class="p-1 rounded mr-2">
                      {{ tag }}</span
                    >
                  </div>
                </div>
              </div>
        </ContentList>
  </main>
</template>

<script lang="ts">
</script>
