// Get all alert class
const items = document.getElementsByClassName('alert')

for (const item in items) {
    setTimeout(() => {
        const alert = document.getElementsByClassName('alert')[item]
        try {
            // if alert is not returning any error then set the display to none
            alert.style.display = 'none'
        } catch (e) {
            // if any error happens then do nothing
            {}
        }
    }, 4000)
}
