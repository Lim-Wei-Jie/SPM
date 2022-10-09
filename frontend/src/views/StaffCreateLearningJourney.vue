<template>
<!-- eslint-disable -->
    <NavBar/>
    <SearchBar :placeholder="placeholderValue" v-model="searchQuery" />
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import SearchBar from '@/components/SearchBar.vue'
import { useRouter } from 'vue-router'


const router = useRouter()

const placeholderValue = 'Search Job Title..'

function createLearningJourney() {
    router.push('/staff/create')
}

</script>

<style scoped>

</style>