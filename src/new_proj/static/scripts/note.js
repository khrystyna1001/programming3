const handleAddText = () => {
    textContentButton = document.getElementById("addTextButton");
    textContentInput = document.createElement("input");
    textContentButton.replaceWith(textContentInput);
}