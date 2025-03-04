<script setup>
import { RouterView, useRouter } from 'vue-router';
import { onMounted } from 'vue';
import { supabase } from '@/utils/supabase';

const router = useRouter();

// Session auto-refresh setup
onMounted(() => {
  const refreshSession = async () => {
    const { data, error } = await supabase.auth.getSession();
    if (error || !data.session) {
      console.error("Session expired or not found:", error);
      return;
    }

    // Refresh token to keep session active
    const { error: refreshError } = await supabase.auth.refreshSession();
    if (refreshError) {
      console.error("Session refresh failed:", refreshError);
    }
  };

  // Run session refresh every 100 seconds
  setInterval(refreshSession, 100000);
});
</script>

<template>  
  <RouterView />
</template>
