<script setup lang="ts">
const {slug} = useRoute().params
</script>

<template>
  <article class="rounded-2xl">
    <ContentDoc :path="`/posts/${slug}`" v-slot="{ doc }">
      <header>
        <div class="text-center p-5">
          <h1 class="text-4xl font-bold lg:w-2/3 mx-auto">{{ doc.title }}</h1>
          <p class="text-sm mt-2">{{ doc.date }}</p>
        </div>
        <img
          v-if="doc.thumbnail"
          :src="doc.thumbnail"
          :alt="doc.title"
          class="w-full"
        />
      </header>
      <div class="mt-4 content p-5">
        <ContentRenderer :value="doc" />
      </div>
    </ContentDoc>
  </article>
</template>
