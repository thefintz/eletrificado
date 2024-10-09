<script setup lang="ts">
definePageMeta({ auth: false });
const {slug} = useRoute().params
</script>

<template>
  <article class="rounded-2xl mx-auto max-w-4xl px-4 py-8">
    <ContentDoc :path="`/posts/${slug}`" v-slot="{ doc }">
      <header>
        <div class="text-center p-5">
          <h1 class="lg:text-4xl font-bold lg:w-3/4 mx-auto text-3xl">{{ doc.title }}</h1>
          <p class="text-sm mt-2">{{ doc.date.split(' ')[0] }}</p>
          <p class="mt-8 text-left lg:w-3/4 mx-auto text-lg italic leading-relaxed">{{ doc.description }}</p>
        </div>
        <img
          v-if="doc.thumbnail"
          :src="doc.thumbnail"
          :alt="doc.title"
          class="mx-auto md:w-3/4 sm:w-full rounded-xl shadow-lg mb-4"
        />
      </header>
      <div class="mt-4 content p-5 text-left">
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

.content ul,
.content ol {
  @apply list-inside list-disc pl-4;
}

.content ul li,
.content ol li {
  @apply mb-3 text-base;
}

.content strong {
  @apply font-bold;
}

.content em {
  @apply italic;
}

.content h1 {
  @apply text-3xl font-bold;
}
.content h2 {
  @apply text-2xl font-bold mt-8;
}
.content h3 {
  @apply text-xl font-bold mt-8;
}
.content h4 {
  @apply text-lg font-bold mt-8;
}
.content h5 {
  @apply text-base font-bold mt-8;
}
</style>