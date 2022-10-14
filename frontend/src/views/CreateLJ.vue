<template>
    <!-- eslint-disable -->
    <NavBar/>
    <div class="container mx-auto my-8 flex flex-col">
        <!-- Breadcrumbs -->
        <div class="text-sm breadcrumbs">
            <ul>
                <li @click="HomePage"><a>Home</a></li> 
                <li @click="JobRolePage"><a>Job Role</a></li> 
                <li> {{roleDetailsName}} </li>
            </ul>
        </div>
        <!-- Role Name -->
        <div class="grid grid-cols-2 my-4">
            <p class="text-3xl font-bold underline underline-offset-8">
                {{roleDetailsName}}
            </p>
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
            <div v-for="(courseList, skillName) in LearningJourney.skills" class="bg-gray-300 rounded-lg my-6 p-8 space-y-4">
                <p class="text-lg font-normal">
                    {{ skillName }}
                </p>
                <div class="grid grid-cols-3 gap-6">
                    <div v-if="courseList != {}" class="flex " v-for="(courseDes, courseName) in courseList">
                        <label class="btn btn-lg w-11/12 modal-btn" for="my-modal" @click="handleJobRoleClick(jobRole)">
                            {{courseName}}
                        </label>

                        <!-- modal pop up to delete course-->
                        <input type="checkbox" id="my-modal" class="modal-toggle" />
                        <div class="modal">
                            <div class="modal-box">
                                <h3 class="font-bold text-lg">{{ courseName }}</h3>
                                <p class="py-4">{{ courseDes }}</p>
                                <div class="modal-action">
                                <label for="my-modal" class="btn btn-outline btn-error" @click="deleteCourse(courseName)">Remove Course</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <label for="addCourseModal" class="modal-btn btn btn-lg btn-outline w-11/12">Add Course</label>
                    <!-- modal pop up to add course-->
                    <input type="checkbox" id="addCourseModal" class="modal-toggle" />
                    <div class="modal">
                        <div class="modal-box h-fit">
                            <h3 class="font-bold text-lg">{{ skillName }}</h3>
                            <ul>
                                <li v-for="(courseDes, courseName) in courseList" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                                    <p>{{ courseName }}</p>
                                    <p>{{ courseDes }}</p>
                                </li>
                            </ul>
                            <div class="modal-action">
                                <label for="my-modal" class="btn btn-outline btn-success" @click="addCourse(courseName)">Add Course</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- send edited data back-->
        <button class="btn btn-outline btn-success" @click="createLJ()">Create Learning Journey</button>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getAllSkills,  getCourses} from "@/endpoint/endpoint.js";

const router = useRouter()
function JobRolePage() {
    router.push('/staff/searchRole')
}
function HomePage() {
    router.push('/staff')
}

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

const LearningJourney = ref({
    jobRoleName: "Mechanical Engineeri",
    skills: {
        "skill1": {},
        "skill2": {},
        "skill3": {}
    }
})

const courseList = ref({
    skillName: "skill",
    courses: {
        "course1": "course description 1",
        "course2": "course description 2",
        "course3": "course description 3",
        "course4": "course description 4",
        "course5": "course description 5"
    }
})

</script>

<style scoped>
</style>