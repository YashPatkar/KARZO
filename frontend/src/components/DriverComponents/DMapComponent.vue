<template>
  <div ref="mapContainer" class="h-[350px] w-full rounded-lg border shadow-md"></div>
</template>

<script setup>
import { ref, onMounted, watch, defineEmits } from 'vue';
import L from 'leaflet';
import axios from 'axios';
import 'leaflet/dist/leaflet.css';

const props = defineProps({
  latitude: Number,
  longitude: Number,
});

const emit = defineEmits(['locationSelected']);
const mapContainer = ref(null);
let map, marker;

onMounted(() => {
  map = L.map(mapContainer.value).setView([props.latitude, props.longitude], 16);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  marker = L.marker([props.latitude, props.longitude], { draggable: true }).addTo(map);

  marker.on('dragend', () => {
    const { lat, lng } = marker.getLatLng();
    updateLocation(lat, lng);
  });

  map.on('click', (event) => {
    const { lat, lng } = event.latlng;
    marker.setLatLng([lat, lng]);
    updateLocation(lat, lng);
  });
});

const updateLocation = async (lat, lng) => {
  try {
    const { data } = await axios.get(
      `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`
    );
    const address = data.display_name || 'Unknown location';
    emit('locationSelected', { lat, lng, address });
  } catch (error) {
    console.error('Error fetching address:', error);
  }
};

watch(() => [props.latitude, props.longitude], ([newLat, newLng]) => {
  if (map) {
    map.setView([newLat, newLng], 16);
    marker.setLatLng([newLat, newLng]);
  }
});
</script>
