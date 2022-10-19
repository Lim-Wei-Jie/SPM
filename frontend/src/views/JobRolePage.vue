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
                {{roleDetailsDesc}}. The Software Engineer / Officer (Engineering Procurement) is responsible for providing administrative support for procurement activities. He/She coordinates with internal teams to gather requirements for procurement, with
                vendors for managing delivery schedules, and prepares purchase orders. He maintains documents and reports schedules material purchases and deliveries and performs verification of current inventory. He is comfortable in engaging and interacting with internal and external stakeholders, and is able to multi-task in a fast-paced work environment.
            </p>
        </div>
        <!-- Skills -->
        <div class="space-y-3 my-4">
            <p class="text-2xl font-medium">
                Skills
            </p>
            <!-- Skills component -->
            <div class="bg-gray-700 rounded-lg my-6 p-8" v-for="skillName in skillNames">
                <div class="font-medium text-lg mb-5">
                    {{skillName}}
                </div>
                <div class="grid grid-cols-3 gap-6">
                    <div class="flex justify-evenly bg-gray-800 rounded-lg">
                        {{coursesBySkillID}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getSkillsByRole, getCoursesBySkill } from "@/endpoint/endpoint.js";

const router = useRouter()

const props = defineProps({
    jobRoleName: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

// can try reactive()
const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()
const skillNames = ref([])
// const skillIDs = ref([])
const coursesBySkillID = ref({}) // key=skillName, value=courseName

;(async() => {
    await Promise.all([
        // get role name, ID, and description
        getRoleDetails(roleName)
        .then((role) => {
            roleDetailsName.value = role.Role_Name
            roleDetailsID.value = role.Role_ID
            roleDetailsDesc.value = role.Role_Desc

            // get skills with role ID
            getSkillsByRole(roleDetailsID.value)
            .then((data) => {
                for (var each of data) {
                    skillNames.value.push(each.Skill_name)

                    // get courses with skill IDs
                    const skillID = each.Skill_id
                    const skillName = each.Skill_name
                    

                    getCoursesBySkill(skillID)
                    .then((data) => {
                        for (var each of data) {
                            // check if skillId exist in object
                            if (coursesBySkillID.value[skillName]) {
                                coursesBySkillID.value[skillName].push(each.Course_Name)
                            } else {
                                coursesBySkillID.value[skillName] = [each.Course_Name]
                            }
                        }
                    })
                    .catch((err) => {
                        console.log(err);
                    })
                }

            })
            .catch((err) => {
                console.log(err);
            })

        })
        .catch((err) => {
            console.log(err);
        }),
        
    ]);
})();



function handleEditClick() {
    router.push({
        path: '/editRole'
    })
}

</script>

<style scoped>
</style>