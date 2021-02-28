window.onload = () => {
  const firstJobObj = document.getElementById("jobToSkill1");
  const firstSkillsObj = document.getElementById("resultSkillBox1");
  const secondJobObj = document.getElementById("jobToSkill2");
  const secondSkillsObj = document.getElementById("resultSkillBox2");
  const thirdJobObj = document.getElementById("jobToSkill3");
  const thirdSkillsObj = document.getElementById("resultSkillBox3");

  if (firstJobObj.getElementsByTagName("div")[0].innerText !== "-") {
    firstJobObj.addEventListener("click", () => {
      firstSkillsObj.style.display = "block";
      secondSkillsObj.style.display = "none";
      thirdSkillsObj.style.display = "none";
      checkSkillsObj();
    });
  }
  if (secondJobObj.getElementsByTagName("div")[0].innerText !== "-") {
    secondJobObj.addEventListener("click", () => {
      firstSkillsObj.style.display = "none";
      secondSkillsObj.style.display = "block";
      thirdSkillsObj.style.display = "none";
      checkSkillsObj();
    });
  }
  if (thirdJobObj.getElementsByTagName("div")[0].innerText !== "-") {
    thirdJobObj.addEventListener("click", () => {
      firstSkillsObj.style.display = "none";
      secondSkillsObj.style.display = "none";
      thirdSkillsObj.style.display = "block";
      checkSkillsObj();
    });
  }

  checkSkillsObj = () => {
    firstJobObj.getElementsByTagName("div")[0].style.color = "";
    firstJobObj.style.border = "";
    firstJobObj.style.backgroundColor = "";
    secondJobObj.getElementsByTagName("div")[0].style.color = "";
    secondJobObj.style.border = "";
    secondJobObj.style.backgroundColor = "";
    thirdJobObj.getElementsByTagName("div")[0].style.color = "";
    thirdJobObj.style.border = "";
    thirdJobObj.style.backgroundColor = "";
    if (firstSkillsObj.style.display !== "none") {
      firstJobObj.getElementsByTagName("div")[0].style.color = "#000";
      firstJobObj.style.border = "1px solid #777";
      firstJobObj.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
    } else if (secondSkillsObj.style.display !== "none") {
      secondJobObj.getElementsByTagName("div")[0].style.color = "#000";
      secondJobObj.style.border = "1px solid #777";
      secondJobObj.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
    } else if (thirdSkillsObj.style.display !== "none") {
      thirdJobObj.getElementsByTagName("div")[0].style.color = "#000";
      thirdJobObj.style.border = "1px solid #777";
      thirdJobObj.style.backgroundColor = "rgba(0, 0, 0, 0.1)";
    }
  };
  checkSkillsObj();
};
