window.onload = () => {
  const firstJobObj = document.getElementById("job1");
  const firstPostsObj = document.getElementById("resultPosts1");
  const secondJobObj = document.getElementById("job2");
  const secondPostsObj = document.getElementById("resultPosts2");
  const thirdJobObj = document.getElementById("job3");
  const thirdPostsObj = document.getElementById("resultPosts3");

  firstJobObj.addEventListener("click", () => {
    firstPostsObj.style.display = "block";
    secondPostsObj.style.display = "none";
    thirdPostsObj.style.display = "none";
    checkPostsObj();
  });
  secondJobObj.addEventListener("click", () => {
    firstPostsObj.style.display = "none";
    secondPostsObj.style.display = "block";
    thirdPostsObj.style.display = "none";
    checkPostsObj();
  });
  thirdJobObj.addEventListener("click", () => {
    firstPostsObj.style.display = "none";
    secondPostsObj.style.display = "none";
    thirdPostsObj.style.display = "block";
    checkPostsObj();
  });

  checkPostsObj = () => {
    firstJobObj.getElementsByTagName("div")[1].style.color = "";
    firstJobObj.style.border = "";
    firstJobObj.style.backgroundColor = "";
    secondJobObj.getElementsByTagName("div")[1].style.color = "";
    secondJobObj.style.border = "";
    secondJobObj.style.backgroundColor = "";
    thirdJobObj.getElementsByTagName("div")[1].style.color = "";
    thirdJobObj.style.border = "";
    thirdJobObj.style.backgroundColor = "";
    if (firstPostsObj.style.display !== "none") {
      firstJobObj.getElementsByTagName("div")[1].style.color = "#000";
      firstJobObj.style.border = "1px solid rgb(31, 211, 243)";
      firstJobObj.style.backgroundColor = "rgb(161, 221, 231)";
    } else if (secondPostsObj.style.display !== "none") {
      secondJobObj.getElementsByTagName("div")[1].style.color = "#000";
      secondJobObj.style.border = "1px solid rgb(31, 211, 243)";
      secondJobObj.style.backgroundColor = "rgb(161, 221, 231)";
    } else if (thirdPostsObj.style.display !== "none") {
      thirdJobObj.getElementsByTagName("div")[1].style.color = "#000";
      thirdJobObj.style.border = "1px solid rgb(31, 211, 243)";
      thirdJobObj.style.backgroundColor = "rgb(161, 221, 231)";
    }
  };
  checkPostsObj();
};
