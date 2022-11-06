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
                reject(err.response.data)
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
                reject(err.response.data)
            })
    })
}

// Create job role
export function createRole(roleDetails, addSkillsIDArr) {
    const addSkills = JSON.parse(JSON.stringify(addSkillsIDArr))

    let createEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/create/${roleDetails.roleName}/${roleDetails.roleDesc}`
    let assignAddEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/roleassignskills/${roleDetails.roleID}/${addSkills}`

    // return new Promise((resolve, reject) => {
    //     Promise.allSettled([
    //         axios.put(createEndpoint),
    //         axios.post(assignAddEndpoint)
    //     ])
    //     .then((res) => {
    //         resolve(res[0].value.data.data)
    //     })
    //     // need to catch duplicate role name error
    //     .catch((err) => {
    //         reject(err)
    //     })
    // })
}

// Update job role
export function updateRole(roleDetails, removeSkillsIDArr, addSkillsIDArr) {
    const removeSkills = JSON.parse(JSON.stringify(removeSkillsIDArr))
    const addSkills = JSON.parse(JSON.stringify(addSkillsIDArr))
    return new Promise((resolve, reject) => {
        if (roleDetails) {
            let updateEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/update/${roleDetails.roleID}/${roleDetails.roleName}/${roleDetails.roleDesc}`
            axios
                .put(updateEndpoint)
                .then((res) => {
                    resolve(res.data.data)
                })
                .catch((err) => {
                    reject(err)
                })
    
        } else {
    
        }
        
        
    })
    
    // let assignRemoveEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/roledeleteskills/${roleDetails.roleID}/${removeSkills}`
    // let assignAddEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/role/roleassignskills/${roleDetails.roleID}/${addSkills}`

    // // check if removeSkills and addSkills not empty, then call respectively route
    // return new Promise((resolve, reject) => {
    //     Promise.allSettled([
    //         axios.put(updateEndpoint),
    //         axios.post(assignRemoveEndpoint),
    //         axios.post(assignAddEndpoint)
    //     ])
    //     .then((res) => {
    //         resolve(res[0].value.data.data)
    //     })
    //     .catch((err) => {
    //         // need to catch duplicate role name error
    //         reject(err)
    //     })
    // })
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

// Delete skill

// Get all courses
export function getAllCourses() {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT}/course`
        axios
            .get(apiEndpoint)
            .then((res) => {
                resolve(res.data.courses)
            })
            .catch((err) => {
                console.log(err);
                reject('Fail to fetch all courses, check WAMP/MAMP server')
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


// Mapping skills to role
export function createLJ2(staffID, roleID) {
    return new Promise((resolve, reject) => {
        let apiEndpoint = `${import.meta.env.VITE_APP_DEV_API_ENDPOINT_MANAGER}/AddLJAssign/${staffID}/${roleID}`
        axios
            .post(apiEndpoint)
            .then((res) => {
                resolve(res)
            })
            .catch((err) => {
                console.log(err.message);
                reject('Fail to fetch all skills, check WAMP/MAMP server')
            })
    })
}