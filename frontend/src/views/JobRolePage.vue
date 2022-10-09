<template>
<!-- eslint-disable -->
    <NavBar/>
    {{roleDetails}}
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
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

const roleDetails = ref()

onMounted(async() => {
    await getRoleDetails(roleName)
    .then((role) => {
        roleDetails.value = role
    }).catch((err) => {
        console.log(err);
    });
});

</script>

<style scoped>
</style>