<script setup lang="ts">
definePageMeta({ auth: false });
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
          class="lg:w-1/2 mx-auto md:w-3/4 sm:w-full rounded-xl shadow-lg mb-4"
        />
      </header>
      <div class="mt-4 content p-5">
        <ContentRenderer :value="doc" />
      </div>
    </ContentDoc>
  </article>
</template>

<style>
.content p:not(:last-child),
.content li:not(:last-child),
.content blockquote:not(:last-child),
.content h1:not(:last-child),
.content h2:not(:last-child),
.content h3:not(:last-child),
.content h4:not(:last-child),
.content pre:not(:last-child),
.content table:not(:last-child) {
  @apply mb-4;
}

.content h1 {
  @apply text-3xl font-bold;
}
.content h2 {
  @apply text-2xl font-bold;
}
.content h3 {
  @apply text-xl font-bold;
}
.content h4 {
  @apply text-lg font-bold;
}
.content h5 {
  @apply text-base font-bold;
}
</style>