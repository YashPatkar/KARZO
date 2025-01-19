<script setup>
import { ref } from 'vue';
import ApplicationLayoutComponent from '@/components/ApplicationComponent/applicationLayoutComponent.vue';

const state = ref('');
const city = ref('');
const startDate = ref('');
const endDate = ref('');
const time = ref('');
const description = ref('');
const location = ref('');
const startDateMenu = ref(false);
const endDateMenu = ref(false);

const states = ref(['California', 'Texas', 'New York']); // Example data
const cities = ref(['Los Angeles', 'Houston', 'New York City']); // Example data
const locations = ref(['Location 1', 'Location 2', 'Location 3']); // Example data

const submitForm = () => {
    // Handle form submission
    console.log({
        state: state.value,
        city: city.value,
        startDate: startDate.value,
        endDate: endDate.value,
        time: time.value,
        description: description.value,
        location: location.value,
    });
};
</script>

<template>
    <ApplicationLayoutComponent>
        <v-form>
            <v-row>
                <v-col cols="12" md="6">
                    <v-autocomplete
                        label="State"
                        v-model="state"
                        :items="states"
                        item-text="name"
                        item-value="name"
                    ></v-autocomplete>
                </v-col>
                <v-col cols="12" md="6">
                    <v-autocomplete
                        label="City"
                        v-model="city"
                        :items="cities"
                        item-text="name"
                        item-value="name"
                    ></v-autocomplete>
                </v-col>
                <v-col cols="12" md="6">
                    <v-menu
                        ref="startDateMenu"
                        v-model="startDateMenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="startDate"
                                label="Start Date"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker v-model="startDate" @input="startDateMenu = false"></v-date-picker>
                    </v-menu>
                </v-col>
                <v-col cols="12" md="6">
                    <v-menu
                        ref="endDateMenu"
                        v-model="endDateMenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="endDate"
                                label="End Date"
                                prepend-icon="mdi-calendar"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                        </template>
                        <v-date-picker v-model="endDate" @input="endDateMenu = false"></v-date-picker>
                    </v-menu>
                </v-col>
                <v-col cols="12" md="6">
                    <v-time-picker v-model="time" label="Time"></v-time-picker>
                </v-col>
                <v-col cols="12">
                    <v-textarea label="Description" v-model="description"></v-textarea>
                </v-col>
                <v-col cols="12">
                    <v-autocomplete
                        label="Location"
                        v-model="location"
                        :items="locations"
                        item-text="name"
                        item-value="name"
                    ></v-autocomplete>
                </v-col>
            </v-row>
            <v-btn color="primary" @click="submitForm">Submit</v-btn>
        </v-form>
    </ApplicationLayoutComponent>
</template>