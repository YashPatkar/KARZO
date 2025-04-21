<script setup>
import { onMounted, ref } from 'vue'
import { gsap } from 'gsap'

const container = ref(null)

onMounted(() => {
  gsap.from(container.value.children, {
    opacity: 0,
    y: 50,
    duration: 0.8,
    stagger: 0.2,
    ease: 'power2.out',
  })
})
</script>

<template>
  <div class="bg-gray-100">
    <div ref="container" class="h-screen flex flex-col justify-center items-center">
      <h1 class="text-8xl font-bold text-gray-800">404</h1>
      <p class="text-4xl font-medium text-gray-800">Page Not Found</p>
      <a href="/" class="mt-4 text-xl text-blue-600 hover:underline">Go back home - Karzo</a>
    </div>
  </div>
</template>
