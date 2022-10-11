<template>
<!-- eslint-disable -->
    <NavBar/>
    <div class="container mx-auto my-8 ">
        <!-- Breadcrumbs -->
        <div class="text-sm breadcrumbs">
            <ul>
                <li><a>Home</a></li> 
                <li><a>Job Role</a></li> 
                <li> {{roleDetailsName}} </li>
            </ul>
        </div>
        <!-- Role Name -->
        <div class="grid grid-cols-2 my-4">
            <p class="text-3xl font-bold underline underline-offset-8">
                {{roleDetailsName}}
            </p>
            <button @click="handleEditClick" class="btn btn-circle place-self-end">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
            </button>
        </div>
        <!-- Role Desc -->
        <div class="space-y-2 my-4 w-4/6">
            <p class="font-medium text-lg">
                Job Role Description
            </p>
            <p>
                {{roleDetailsDesc}}The Software Engineer / Officer (Engineering Procurement) is responsible for providing administrative support for procurement activities. He/She coordinates with internal teams to gather requirements for procurement, with
                vendors for managing delivery schedules, and prepares purchase orders. He maintains documents and reports schedules material purchases and deliveries and performs verification of current inventory. He is comfortable in engaging and interacting with internal and external stakeholders, and is able to multi-task in a fast-paced work environment.
            </p>
        </div>
        <!-- Skills -->
        <div class="space-y-3 my-4">
            <p class="text-2xl font-medium">
                Skills
            </p>
            <div class="grid grid-cols-3 gap-6 bg-gray-700 rounded-lg my-6 p-8">
                <div class="flex justify-evenly">
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails } from "@/endpoint/endpoint.js";

const router = useRouter()

const props = defineProps({
    jobRoleName: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()

onBeforeMount(async() => {
    await getRoleDetails(roleName)
    .then((role) => {
        roleDetailsName.value = role.Role_Name
        roleDetailsID.value = role.Role_ID
        roleDetailsDesc.value = role.Role_Desc
    }).catch((err) => {
        console.log(err);
    });
});

function handleEditClick() {
    router.push({
        path: '/editRole'
    })
}

</script>

<style scoped>
</style>