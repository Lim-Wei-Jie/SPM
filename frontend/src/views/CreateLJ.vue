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
            <!--
            <div v-for="skill in skillsList" class="bg-gray-300 rounded-lg my-6 p-8 space-y-4"></div>
            -->
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
                    <label for="addCourseModal" class="modal-btn btn btn-lg btn-outline w-11/12" @click="getAllCourses(skill[0])">Add Course</label>
                    <!-- modal pop up to add course-->
                    <input type="checkbox" id="addCourseModal" class="modal-toggle" />
                    <div class="modal">
                        <div class="modal-box h-fit w-11/12">
                            <h3 class="font-bold text-lg">{{ skillName }}</h3>
                            <!--
                            <h3 class="font-bold text-lg">{{ skill[1] }}</h3>
                            -->
                            <ul>
                                <!--
                                <li v-for="course in courseList" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                                -->
                                <li v-for="(courseDes, courseName) in coursesList.courses" class="bg-slate-50 hover:shadow-lg hover:bg-slate-100 px-5 py-3">
                                    <div class="flex justify-between">
                                        <!--
                                        <p>{{ course[1] }}</p>
                                        -->
                                        <p>{{ courseName }}</p>
                                        <!--
                                        <input type="checkbox" v-model="selectedCourses" :id="course[0]" :value="course[1]" class="checkbox" />
                                        -->
                                        <input type="checkbox" v-model="selectedCourses" :id="courseName" :value="courseName" class="checkbox" />
                                    </div>
                                    <!--
                                    <p>{{ course[2] }}</p>
                                    -->
                                    <p>{{ courseDes }}</p>
                                </li>
                            </ul>
                            <p>selected courses: {{selectedCourses}}</p>
                            <div class="modal-action">
                                <!--
                                <label for="addCourseModal" class="btn btn-outline btn-success" @click="addCourse(selectedCourses, skillName)">Add Course</label>
                                -->
                                <label for="addCourseModal" class="btn btn-outline btn-success" @click="addCourse(selectedCourses, skillName)">Add Course</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- send edited data back-->
        <label for="my-modal" class="btn btn-outline btn-success" @click="createLJ()">Create Learning Journey</label>
    </div>
</template>

<script setup>
import NavBar from '@/components/Navbar.vue'
import { ref, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { getRoleDetails, getSkillsByRole,  getCourses} from "@/endpoint/endpoint.js";

//route back for breadcrumb
const router = useRouter()
function HomePage() {
    router.push('/staff')
}
function JobRolePage() {
    router.push('/staff/searchRole')
}


const props = defineProps({
    jobRoleName: {
        type: String
    }
});
// props to be use in script setup, break down proxy
const { jobRoleName } = toRefs(props)
const roleName = JSON.parse(JSON.stringify(jobRoleName))._object.jobRoleName

//JOB ROLE
const roleDetailsName = ref()
const roleDetailsID = ref()
const roleDetailsDesc = ref()

;(async() => {
    await getRoleDetails(roleName)
    .then((role) => {
        roleDetailsName.value = role.Role_Name
        roleDetailsID.value = role.Role_ID
        roleDetailsDesc.value = role.Role_Desc
    }).catch((err) => {
        console.log(err);
    });
})();


//SKILLS
const skillsList = ref()

;(async() => {
    await getSkillsByRole(roleDetailsID)
    .then((skills) => {
        for(var skill of skills){
            var skillDetails = [skill.Skill_ID, skill.Skill_Name, skill.Skill_Desc]
            skillsList.value += skillDetails
        }
    }).catch((err) => {
        console.log(err);
    });
})();

//COURSES
const courseList = ref()

function getAllCourses(skillID) {
    ;(async() => {
        await getCourses(skillID)
        .then((courses) => {
            for (var course of courses) {
                var courseDetails = [course.Course_ID, course.Course_Name, course.Course_Desc]
                courseList += courseDetails
            }
        }).catch((err) => {
            console.log(err);
        });
    })();
}



function addCourse() {

}

function deleteCourse() {

}

function createLJ() {

}


//FAKE DATA
var LearningJourney = ref({
    jobRoleName: "Mechanical Engineeri",
    skills: {
        "skill1": {},
        "skill2": {},
        "skill3": {}
    }
})

const coursesList = ref({
    skillName: "skill",
    courses: {
        "course1": "course description 1",
        "course2": "course description 2",
        "course3": "course description 3",
        "course4": "course description 4",
        "course5": "course description 5"
    }
})

const skillListFake = ref(
    [1, "Facebook", "Duis consequat dui n"],
    [2, "UB04", "Phasellus in felis."],
    [3, "TMA", "In congue. Etiam jus"]
)
const selectedCourses = ref([])


function addCourse(selectedCourses, skillName) {
    for (course in selectedCourses.value) {
        var addCourseDes = coursesList.courses[course]
        console.log(addCourseDes)
    }
    //call backend route
    console.log('done')
    console.log(LearningJourney.value.skills[skillName])
    selectedCourses = []
}


</script>

<style scoped>
</style>