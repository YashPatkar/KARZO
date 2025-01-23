import { defineStore } from "pinia";

export const useEventStore = defineStore('eventStore', {
    state: () => ({
      events: [], // Array to store submitted events
    }),
    actions: {
      addEvent(event) {
        this.events.push(event); // Add event to the state
      },
    },
});