import axios from "axios";

// Get all Job Roles
export function getAllRoles() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all job roles, check WAMP/MAMP server')
            })
    })
}

// Get specific Job Role details using Job Role ID / Name
export function getRoleDetails(jobRoleName) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/name/${jobRoleName}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0])
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch job role details, check WAMP/MAMP server')
            })
    })
}

// Get all skills assigned to Job Role using Job Role ID
export function getSkillsByRole(jobRoleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/getskill/${jobRoleID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Skill)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills by role, check WAMP/MAMP server')
            })
    })
}

// Get all Courses that fulfils the Skill using Skill ID
export function getCoursesBySkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/getcourse/${skillID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Course)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses by skill, check WAMP/MAMP server')
            })
    })
}

// Create job role
export function createRole(newJobRoleData) {
    var role_id = newJobRoleData[0];
    var role_name = newJobRoleData[1];
    var role_des = newJobRoleData[2];
    // var BE_error = false;
    // var job_err_msg = '';

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/${role_id}/${role_name}/${role_des}`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create role, check WAMP/MAMP server')
            })
    })
}

// Update job role
export function updateRole(roleID, skillIDArr) {
    // const roleID = updateDetails
    console.log(JSON.parse(JSON.stringify(skillIDArr)))
    /*
    Will make 3 concurrent API calls for:
    1. Changes in role name and desc
    2. Addition of skills
    3. Removal of skills
    Can use Promise.all() or Axios.all()
    */
}

// Delete job role
export function deleteRole(roleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/delete/${roleID}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to delete role, check WAMP/MAMP server');
            })
    })
}

// Get all Skills
export function getAllSkills() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.books)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}

// Mapping skills to role
export function mapSkillsToJob(skillstoJobRoleData) {
    var role_id = skillstoJobRoleData[0];
    var skills_id = skillstoJobRoleData[1];

    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/roleassignskills/${role_id}/${skills_id}/`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}


// Delete job role
// export function deleteRole(roleDetailsID) {

//     return new Promise((resolve, reject) => {
//         let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/delete/${roleDetailsID}`
//         axios
//         .post(apiEndpoint)
//             .then((res) => {
//                 resolve(res.data)
//             })
//             .catch((err) => {
//                 console.log(err.message);
//                 reject('Fail to create role, check WAMP/MAMP server');
//             })
//     })
// }


// Get specific course using course name
export function getCourseDetails(Course_Name) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/searchcourse/${Course_Name}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
        })
}

//LEARNING JOURNEY

// Get all registration
export function getAllRegistration() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

// Get all registration number
export function getAllRegistrationNo() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.registration.length + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

export function getAllLJPSNo() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/LJPS_Assignment`
            axios
            .get(apiEndpoint)
            .then((res) => {
                var lastLJPS = res.data.data.maps.slice(-1)[0].LJPS_ID

                resolve(lastLJPS + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

// Get registration with Staff ID
export function getRegistration(staffID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration/${staffID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.registration)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

// create registration
export function createRegistration(regID, courseID, staffID, regStatus, completionStatus) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration/addRegis/${regID}/${courseID}/${staffID}/${regStatus}/${completionStatus}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create registration, check WAMP/MAMP server');
            })
    })
}


// Get Learning Journeys with Staff ID
export function getLJs(staffID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/LJAssign/${staffID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.deets)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch learning journeys of staff, check WAMP/MAMP server')
            })
    })
}

// create LJ assignment
export function createLJAssign(courseID, roleID, staffID, ljpsID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/AddLJAssign/${staffID}/${roleID}/${courseID}/${ljpsID}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create registration, check WAMP/MAMP server');
            })
    })
}

export function getRoleNameByID(jobID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/${jobID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0].Role_Name)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getRoleByID(jobID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/${jobID}`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.Role[0])
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getSkillIdByCourseName(CourseID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill_course_assignment`
        axios
            .get(apiEndpoint)
            .then((res) => {
                var assignments = res.data.data.maps
                var b = []
                for (var a of assignments) {
                    if (CourseID == a.Course_ID) {
                        b.push(a.Skill_ID)
                    }
                }
                resolve(b)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch registration of staff, check WAMP/MAMP server')
            })
    })
}

export function getStaffCreate() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/Registration`
            axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.registration.length + 1)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all registrations, check WAMP/MAMP server')
            })
    })
}

// Delete skill
export function deleteSkill(skillID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/delete/${skillID}`
        axios
        .delete(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to delete role, check WAMP/MAMP server');
            })
    })
}

// Get all courses
export function getAllCourses() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/course`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.data.courses)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
            })
    })
}

// Update skill
export function updateSkill(skillID, skillName, skillDesc) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/update/${skillID}/${skillName}/${skillDesc}`
        axios
        .put(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to update skill details, check WAMP/MAMP server');
            })
    })
}

// add courses to skill
export function addCoursesToSkill(skillID, addCourseIDArr) {
    return new Promise((resolve, reject) => {
        const addedCourses = JSON.parse(JSON.stringify(addCourseIDArr._rawValue))
        console.log(addCourseIDArr);
        console.log(addedCourses);
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/skillassigncourse/${skillID}/${addedCourses}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to add courses to skill, check WAMP/MAMP server');
            })
    })
}

// remove course from skill 
export function removeCoursesFromSkill(skillID, removeCourseIDArr) {
    return new Promise((resolve, reject) => {
        const removedCourses = JSON.parse(JSON.stringify(removeCourseIDArr._rawValue))
        console.log(removeCourseIDArr);
        //console.log(addedCourses);
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/skilldeletecourse/${skillID}/${removedCourses}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to remove course from skill, check WAMP/MAMP server');
            })
    })
}

// Create skill
export function createSkill(skillName, skillDesc) {
    return new Promise((resolve, reject) => {
        // const newSkillName = JSON.parse(JSON.stringify(skillName._rawValue));
        // const newSkillDesc = JSON.parse(JSON.stringify(skillDesc._rawValue))
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/skill/${skillName}/${skillDesc}`
        axios
        .post(apiEndpoint)
            .then((res) => {
                resolve(res.data)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to create skill, check WAMP/MAMP server');
            })
    })
}