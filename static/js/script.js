// Ваш файл script.js
document.addEventListener("DOMContentLoaded", function() {
    const deleteButton = document.getElementById("deleteButton");
    const confirmationModal = document.getElementById("confirmationModal");
    const confirmDeleteButton = document.getElementById("confirmDeleteButton");
    const cancelDeleteButton = document.getElementById("cancelDeleteButton");

    deleteButton.addEventListener("click", function() {
        confirmationModal.style.display = "block";
    });

    cancelDeleteButton.addEventListener("click", function() {
        confirmationModal.style.display = "none";
    });

    confirmDeleteButton.addEventListener("click", function() {
        // Відправте запит на видалення, наприклад, через Ajax
        const positionId = "{{ object.pk }}"; // ID позиції, яку ви хочете видалити
        fetch(`/path/to/delete/${positionId}/`)
            .then(response => response.json())
            .then(data => {
                // Обробіть відповідь сервера (якщо потрібно)
                // Наприклад, оновлення списку позицій на сторінці
            })
            .catch(error => console.error("Помилка:", error));

        confirmationModal.style.display = "none";
    });
});
