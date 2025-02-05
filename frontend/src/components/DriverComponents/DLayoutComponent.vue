<script setup>
import { ref, defineAsyncComponent } from 'vue'
const drawer = ref(true)

// Lazy-load components when clicked
const items = ref([
    {
        title: 'Home',
        prependIcon: 'mdi-home',
        to: { name: 'DHomeView' },
        component: defineAsyncComponent(() => import('@/views/DriverViews/DHomeView.vue'))
    },
    {
        title: 'Dashboard',
        prependIcon: 'mdi-view-dashboard-outline',
        to: { name: 'DHomeView' },
        component: defineAsyncComponent(() => import('@/views/DriverViews/DHomeView.vue'))
    },
    {
        title: 'Events',
        prependIcon: 'mdi-account-group',
        to: { name: 'DEventView' },
        component: defineAsyncComponent(() => import('@/views/DriverViews/DEventView.vue'))
    },
    {
        title: 'Events Uploader',
        prependIcon: 'mdi-briefcase-outline',
        to: { name: 'DEventUploadView' },
        component: defineAsyncComponent(() => import('@/views/DriverViews/DEventUploadView.vue'))
    }
])

</script>

<template>
    <v-layout>
        <v-navigation-drawer v-model="drawer">
            <v-list-item class="ma-1" density="compact" v-for="(item, index) in items" :key="index" :to="item.to"
                :title="item.title" :prepend-icon="item.prependIcon" nav />
            <template #append>
                <v-list-item class="ma-2" link nav prepend-icon="mdi-cog-outline" title="Settings" />
            </template>
        </v-navigation-drawer>

        <v-app-bar border="b" class="ps-4" flat>
            <v-app-bar-nav-icon v-if="$vuetify.display.smAndDown" @click="drawer = !drawer" />

            <v-app-bar-title>Application</v-app-bar-title>

            <template #append>
                <v-btn class="text-none me-2" height="48" icon slim>
                    <v-avatar color="surface-light" image="https://cdn.vuetifyjs.com/images/john.png" size="32" />

                    <v-menu activator="parent">
                        <v-list density="compact" nav>
                            <v-list-item append-icon="mdi-cog-outline" link title="Settings" />

                            <v-list-item append-icon="mdi-logout" link title="Logout" />
                        </v-list>
                    </v-menu>
                </v-btn>
            </template>
        </v-app-bar>

        <v-main>
            <slot></slot>
        </v-main>
    </v-layout>
</template>