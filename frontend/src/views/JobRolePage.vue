<template>
<!-- eslint-disable -->
    <NavBar/>
    {{jobRoleName}}
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onMounted } from 'vue'
import { getRoleDetails } from "@/endpoint/endpoint.js";

const props = defineProps({
    jobRoleName: {
        type: String
    }
});

const { jobRoleName } = toRefs(props) // to be use in script setup

const roleDetails = ref() // obj to be retrieve from DB

onMounted(async() => {
    await getRoleDetails(jobRoleName)
    .then((data) => {
        console.log(data);
    }).catch((err) => {
        console.log(err);
    });
})

</script>

<style scoped>
</style>