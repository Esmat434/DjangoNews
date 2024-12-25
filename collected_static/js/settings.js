function toggleEdit(inputId, saveBtnId) {
    let inputField = document.getElementById(inputId);
    let saveBtn = document.getElementById(saveBtnId);

    if (inputField.readOnly) {
        inputField.readOnly = false;
        saveBtn.style.display = "inline-block"; // Show save button
    } else {
        inputField.readOnly = true;
        saveBtn.style.display = "none"; // Hide save button
    }
}

function saveInput(inputId) {
    let inputField = document.getElementById(inputId);
    let saveBtnId = "save" + inputId[inputId.length - 1];
    let saveBtn = document.getElementById(saveBtnId);

    inputField.readOnly = true;
    saveBtn.style.display = "none"; // Hide save button
}