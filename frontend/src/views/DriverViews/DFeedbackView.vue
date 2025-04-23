<script setup>
import { ref } from 'vue'
import api from '@/api'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'

const email = ref(sessionStorage.getItem('driver_email'))
const message = ref('')
const rating = ref(0)
const submitting = ref(false)
const success = ref(null)
const error = ref(null)

const setRating = (value) => {
  rating.value = value
}

const submitFeedback = async () => {
  if (!rating.value) {
    error.value = 'Please rate your experience before submitting.'
    return
  }

  submitting.value = true
  success.value = null
  error.value = null

  try {
    await api.post('/api/driver/feedback/', {
      email: email.value,
      message: message.value,
    })
    success.value = 'Thanks for helping Karzo improve! 💙'
    message.value = ''
    rating.value = 0
  } catch (err) {
    error.value = 'Oops! Something went wrong. Please try again.'
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <DLayoutComponent>
    <div class="max-w-xl mx-auto mt-10 p-6 bg-white rounded-3xl shadow-lg border border-gray-200 transition-all duration-300">
      <div class="text-center mb-6">
        <h1 class="text-3xl font-extrabold text-gray-800 tracking-tight">Feedback for Karzo</h1>
        <p class="text-gray-500 mt-1">Your voice helps us ride better, together 🚀</p>
      </div>

      <form @submit.prevent="submitFeedback" class="space-y-6">
        <!-- Rating -->
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Rate Your Experience</label>
          <div class="flex justify-center gap-2">
            <template v-for="n in 5" :key="n">
              <button
                type="button"
                @click="setRating(n)"
                :class="n <= rating ? 'text-yellow-400' : 'text-gray-300'"
                class="text-3xl focus:outline-none hover:scale-110 transition"
              >
                ★
              </button>
            </template>
          </div>
        </div>

        <!-- Message -->
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Your Feedback</label>
          <textarea
            v-model="message"
            rows="4"
            required
            placeholder="Tell us how we did or how we can improve..."
            class="w-full border border-gray-300 rounded-xl px-4 py-3 text-sm text-gray-800 focus:ring-2 focus:ring-blue-500 focus:outline-none resize-none transition"
          ></textarea>
        </div>

        <!-- Submit -->
        <button
          type="submit"
          :disabled="submitting"
          class="w-full bg-blue-600 text-white py-3 rounded-xl font-medium hover:bg-blue-700 transition disabled:opacity-50"
        >
          {{ submitting ? 'Submitting...' : 'Submit Feedback' }}
        </button>
      </form>

      <!-- Alerts -->
      <transition name="fade">
        <div v-if="success" class="mt-6 flex items-center justify-center gap-2 text-green-700 bg-green-100 rounded-md py-2 px-4">
          <span>✅</span>
          <span>{{ success }}</span>
        </div>
      </transition>

      <transition name="fade">
        <div v-if="error" class="mt-6 flex items-center justify-center gap-2 text-red-700 bg-red-100 rounded-md py-2 px-4">
          <span>⚠️</span>
          <span>{{ error }}</span>
        </div>
      </transition>
    </div>
  </DLayoutComponent>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
