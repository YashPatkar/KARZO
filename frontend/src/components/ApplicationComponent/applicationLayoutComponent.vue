<script setup>
import { ref } from 'vue';

const drawer = ref(true);
const props = defineProps(['breadcrumitem']);

const toggleFullScreen = () => {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
};
</script>

<template>
    <v-app>
        <!-- Sidebar -->
        <v-navigation-drawer v-model="drawer" app width="230">
            <v-list>
                <!-- LOGO -->
                <v-list-item class="justify-center">
                    <v-list-item-title class="text-h6 font-weight-bold">KARZO</v-list-item-title>
                    <v-list-item-subtitle class="text-caption">Your trusted partner</v-list-item-subtitle>
                </v-list-item>
                <v-divider></v-divider>

                <v-list-subheader>Features</v-list-subheader>
                <v-list-item :to="{ name: 'DriverHome' }" title="Home" prepend-icon="mdi-home" />
                <v-list-item :to="{ name: 'DriverEvent' }" title="Event" prepend-icon="mdi-palette" />
                <v-list-item :to="{ name: 'DriverDashboard' }" title="Dashboard" prepend-icon="mdi-format-text" />
                <v-list-item :to="{ name: 'DriverPayment' }" title="Payment" prepend-icon="mdi-currency-usd" />
                <v-list-item :to="{ name: 'DriverEventUploader' }" title="EventUploader" prepend-icon="mdi-currency-usd" />
                
            </v-list>
        </v-navigation-drawer>

        <!-- App Bar -->
        <v-app-bar app dense flat>
            <v-app-bar-nav-icon @click="drawer = !drawer" />
            <v-breadcrumbs>
                <v-breadcrumbs-item>{{ breadcrumitem }}</v-breadcrumbs-item>
            </v-breadcrumbs>
            <v-spacer></v-spacer>
            <div class="app-bar-icons">
                <v-btn icon @click="toggleFullScreen">
                    <v-icon>mdi-fullscreen</v-icon>
                </v-btn>
                <v-btn icon>
                    <v-icon>mdi-bell</v-icon>
                </v-btn>
                <v-btn icon>
                    <v-icon>mdi-email</v-icon>
                </v-btn>
                
                <v-avatar 
                    image="https://cdn.vuetifyjs.com/images/john.png" size="33" class="cursor-pointer app-user-avatar" />
                <!-- <v-list dense>
                        <v-list-item title="Settings" prepend-icon="mdi-cog-outline" />
                        <v-list-item title="Logout" prepend-icon="mdi-logout" />
                </v-list> -->
            </div>
        </v-app-bar>

        <!-- Main Content -->
        <v-main>
            <v-container>
                <slot></slot>
            </v-container>
        </v-main>
    </v-app>
</template>

<style>
.app-bar-icons {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    position: absolute;
    right: -25px;
    top: 0;
    padding: 0 50px;
    height: 100%;
}

.app-user-avatar {
    margin-left: 10px;
}
</style>
