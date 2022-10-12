<template>
<!-- eslint-disable -->
    <NavBar/>
    <Hero v-if="numOfLJ == 0" :title="title" :button="button" @click="searchJobRole"/>
    <div v-else class="container mx-auto my-8">
        <p class="text-2xl font-bold">
            Learning Journey Progress
        </p>
        <LearningJourney></LearningJourney>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import Hero from '@/components/Hero.vue'
import LearningJourney from '@/components/LearningJourney.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue';

const router = useRouter()

//check for existing LJ
const numOfLJ = ref(3)

//no existing LJ
const title = 'You have no learning journey'
const button = 'Create now'

function searchJobRole() {
    router.push('/staff/searchRole')
}

</script>

<style scoped>

</style>