<template>
<!-- eslint-disable -->
    <NavBar/>
    {{jobRole}}
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref } from 'vue'

const props = defineProps({
    jobRole: {
        type: String,
        default: ''
    }
});

</script>

<style scoped>
</style>