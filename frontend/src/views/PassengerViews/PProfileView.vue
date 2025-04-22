<template>
  <PLayoutComponent>
    <div class="bg-gray-100 min-h-screen py-10 px-4 flex justify-center items-center">
      <div class="w-full max-w-4xl bg-white rounded-3xl shadow-xl p-10">
        <!-- Header -->
        <div class="text-center mb-10">
          <h2 class="text-4xl font-extrabold text-gray-800">Passenger Profile</h2>
          <p class="text-sm text-gray-500 mt-1">Manage your account information with ease</p>
        </div>

        <!-- Profile Image -->
        <div class="flex justify-center mb-10">
          <div class="relative w-40 h-40 rounded-full overflow-hidden border-4 border-purple-600 shadow-lg group">
            <img
              v-if="profilePreview"
              :src="profilePreview"
              alt="Profile"
              class="w-full h-full object-cover"
            />
            <i
              v-else
              class="fas fa-user text-gray-300 text-6xl absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
            ></i>
            <input
              type="file"
              accept="image/*"
              @change="handleProfilePhotoChange"
              class="absolute inset-0 opacity-0 cursor-pointer z-10"
            />
            <div
              class="absolute inset-0 bg-black bg-opacity-30 text-white opacity-0 group-hover:opacity-100 transition flex items-center justify-center text-sm font-medium"
            >
              Change Photo
            </div>
          </div>
        </div>

        <!-- Form Fields -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Full Name</label>
            <input
              v-model="editedName"
              type="text"
              class="w-full px-4 py-3 rounded-xl border border-gray-300 shadow-sm focus:ring-2 focus:ring-purple-500 focus:outline-none text-gray-800"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Email Address</label>
            <input
              :value="passenger.email"
              type="email"
              disabled
              class="w-full px-4 py-3 rounded-xl bg-gray-100 text-gray-500 border border-gray-200 shadow-inner"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Phone Number</label>
            <input
              :value="passenger.phone"
              type="tel"
              disabled
              class="w-full px-4 py-3 rounded-xl bg-gray-100 text-gray-500 border border-gray-200 shadow-inner"
            />
          </div>

          <div class="md:col-span-2">
            <label class="block text-sm font-semibold text-gray-700 mb-2">Address</label>
            <textarea
              :value="passenger.address"
              rows="3"
              disabled
              class="w-full px-4 py-3 rounded-xl bg-gray-100 text-gray-500 border border-gray-200 shadow-inner resize-none"
            ></textarea>
          </div>
        </div>

        <!-- Save Button -->
        <div class="mt-10 text-center">
          <button
            @click="saveProfile"
            :disabled="saving"
            class="inline-flex items-center gap-2 px-6 py-3 bg-purple-600 hover:bg-purple-700 text-white text-base font-semibold rounded-xl shadow-lg transition duration-200"
          >
            <i class="fas fa-save"></i>
            {{ saving ? 'Saving...' : 'Save Changes' }}
          </button>
        </div>
      </div>
    </div>
  </PLayoutComponent>
</template>

<script setup>
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue'
import { ref, onMounted } from 'vue'
import api from '@/api'

const passenger = ref({})
const editedName = ref('')
const profilePreview = ref('')
const selectedImage = ref(null)
const saving = ref(false)

const fetchPassengerProfile = async () => {
  try {
    const email = sessionStorage.getItem('passenger_email')
    if (!email) {
      window.location.href = '/'
      return
    }

    const response = await api.get('/api/passenger/passenger-profile/', {
      params: { email }
    })

    passenger.value = response.data.data
    editedName.value = passenger.value.name
    profilePreview.value = passenger.value.profile_photo
  } catch (error) {
    console.error('Failed to fetch passenger data:', error)
    alert('Failed to load passenger profile. Please try again.')
  }
}

onMounted(() => {
  fetchPassengerProfile()
})

const handleProfilePhotoChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    selectedImage.value = file
    profilePreview.value = URL.createObjectURL(file)
    console.log(profilePreview.value);  // Check if the preview URL is set
  }
}

const uploadImageToImgBB = async () => {
  if (!selectedImage.value) return null

  const formData = new FormData()
  formData.append('image', selectedImage.value)

  try {
    const response = await fetch(
      `https://api.imgbb.com/1/upload?key=${import.meta.env.VITE_IMGBB_API_KEY}`,
      {
        method: 'POST',
        body: formData
      }
    )

    const data = await response.json()
    if (data.success) {
      return data.data.url
    }
  } catch (error) {
    console.error('Error uploading image:', error)
  }

  return null
}

const saveProfile = async () => {
  saving.value = true
  try {
    const profilePhotoUrl = await uploadImageToImgBB()

    const updatedData = {
      name: editedName.value,
      profile_photo: profilePhotoUrl || passenger.value.profile_photo
    }

    await api.put('/api/passenger/passenger-profile/', {
      ...updatedData,
      email: passenger.value.email
    })

    alert('Profile updated successfully!')
  } catch (err) {
    console.error('Error updating profile:', err)
    alert('Something went wrong!')
  } finally {
    saving.value = false
  }
}
</script>
