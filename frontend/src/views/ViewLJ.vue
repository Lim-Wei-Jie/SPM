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
            <button @click="handleEditClick(ljpsID, jobRoleID)" class="btn btn-circle place-self-end">
                <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z"></path></svg>
            </button>
        </div>
        <!-- Role Desc -->
        <div class="space-y-2 my-4 w-4/6">
            <p class="font-medium text-lg">
                Job Role Description
            </p>
            <p>
                {{roleDetailsDesc}}
            </p>
        </div>
        <!-- Skills -->
        <div class="space-y-3 my-4">
            <p class="text-2xl font-medium">
                Skills
            </p>
            
            <div v-for="skill in skillsList" class="bg-gray-300 rounded-lg my-6 p-8 space-y-4">
                <p class="text-lg font-normal">
                    {{ skill.skill_name }}
                </p>
                <div class="grid grid-cols-3 gap-6">
                    <li v-for="course in skill.courses_selected" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                        <div class="flex justify-between">
                            <div>
                                <p class="font-medium">{{ course.course_id}} - {{ course.course_name }}</p>
                                <p class="font-light">{{ course.course_desc }}</p>
                            </div>
                        </div>
                    </li>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { getLJs, getRoleByID, getSkillsByRole, getCoursesBySkill, getSkillIdByCourseName } from "@/endpoint/endpoint.js";

const router = useRouter()
function JobRolePage() {
    router.push('/staff/searchRole')
}
function HomePage() {
    router.push('/staff')
}

const props = defineProps({
    jobRoleID: {
        type: String
    },
    ljpsID: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleID } = toRefs(props)
const { ljpsID } = toRefs(props)


const staffID = '130003'
const courseList = ref()
const roleDetailsName = ref()
const roleDetailsDesc = ref()

const skillsIdList = []
;(async() => {
    await getSkillsByRole(jobRoleID.value)
    .then((skills) => {
        for(var skill of skills){
            skillsIdList.push(skill.Skill_ID)
        }
    }).catch((err) => {
        console.log(err);
    });
})();

// REGISTERED COURSES
const registeredCourses = ref([])
const registeredCourses2 = ref([])
const registeredCourses3 = ref([])
const skillsList = ref([])

;(async() => {
try {
    //SHOW JOB DETAILS
    const role = await getRoleByID(jobRoleID.value)
    roleDetailsName.value = role.Role_Name
    roleDetailsDesc.value = role.Role_Desc

    //SHOW REGISTERED COURSES
    const resA = await getLJs(staffID)
    for (var course of resA[jobRoleID.value]) {
        registeredCourses.value.push(course)
    }

    for (var a in registeredCourses.value) {
        var courseName = registeredCourses.value[a][2]
        const skillIDs = await getSkillIdByCourseName(courseName)
        var temp = 0
        for (var x in skillIDs) {
            for (var y in skillsIdList) {
                if (skillIDs[x] == skillsIdList[y]) {
                    if (temp == 0) {
                        registeredCourses2.value.push(skillIDs[x])
                        temp += 1
                    }
                }
            }
        }
    }

    const skills = await getSkillsByRole(jobRoleID.value)
    for (var skill of skills) {
        var courses = await getCoursesBySkill(skill.Skill_ID)
        for (var course1 of courses) {
            for (var course2 of registeredCourses.value) {
                var course_ID = course2[2]
                if (course_ID == course1.Course_ID) {
                    var courseDetails = {
                        course_name: course1.Course_Name,
                        course_id: course1.Course_ID,
                        course_desc: course1.Course_Desc
                    }
                    registeredCourses3.value.push(courseDetails)
                }
            }
        }
        console.log(registeredCourses3.value[2])
        var regCourses = []
        for (let i = 0; i < registeredCourses2.value.length; i++) {
            if (registeredCourses2.value[i] == skill.Skill_ID) {
                console.log(i)
                console.log(registeredCourses.value[i], skill.Skill_ID)
                console.log(registeredCourses3.value[i])
                regCourses.push(registeredCourses3.value[i])
            }
        }

        var skillDetails = {
                skill_id: skill.Skill_ID,
                skill_name: skill.Skill_Name,
                skill_desc: skill.Skill_Desc,
                courses_available: courseList,
                courses_selected: regCourses
            }
        skillsList.value.push(skillDetails) 
    }
}
catch(err) {
    console.log(err);
}
})();

function handleEditClick(ljpsID, jobRoleID) {
    router.push(`staff/edit/${ljpsID}/${jobRoleID}`)
}

</script>

<style scoped>
</style>