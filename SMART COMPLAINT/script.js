// ----- Student Login (Anonymous, no password) -----
const studentLoginForm = document.getElementById('studentLoginForm');
if(studentLoginForm){
    studentLoginForm.addEventListener('submit', function(e){
        e.preventDefault();
        let username = document.getElementById('studentUsername').value.trim();
        if(username === "") username = "Anonymous";

        // Save username temporarily in localStorage for reference in complaint page
        localStorage.setItem('currentStudent', username);

        // Redirect to complaint submission form
        window.location.href = "complaint_form.html";
    });
}
