window.onload = () => {
  const skillContainer = document.getElementById("skillContainer");
  const jobContainer = document.getElementById("jobContainer");
  const skillLayer = document.getElementById("skillLayer");
  const jobLayer = document.getElementById("jobLayer");
  const skillBtn = document.getElementById("skillBtn");
  const jobBtn = document.getElementById("jobBtn");
  const selectedSkillObjs = document.getElementsByClassName(
    "selected-skill-item"
  );
  const selectedJobObjs = document.getElementsByClassName("selected-job-item");
  const categories = document.getElementsByClassName("category");
  const skillItems = document.getElementsByClassName("skill-item");
  const jobItems = document.getElementsByClassName("job-item");
  const plusOption = document.getElementById("plusOption");
  const favorOptionContainer = document.getElementById("favorOptionContainer");
  const firstOption = document.getElementById("firstOption");
  const secondOption = document.getElementById("secondOption");
  const thirdOption = document.getElementById("thirdOption");
  let selectedSkillCount = 0;
  let selectedJobCount = 0;
  let selectedJobList = [];
  // 검색 관련
  document.getElementById("searchJobBtn").addEventListener("click", () => {
    selectedJobs = [];
    selectedJobsStr = [];
    selectedJob1 = "";
    selectedJob2 = "";
    selectedJob3 = "";
    count = 0;
    for (let item of selectedJobObjs) {
      if (item.style.display === "grid") {
        // jobId = String(item.id).replace("selectedJob", "");
        // selectedJobs.push(jobId);
        if (count === 0) {
          selectedJob1 = item.innerText;
          count++;
        } else if (count === 1) {
          selectedJob2 = item.innerText;
          count++;
        } else if (count === 2) {
          selectedJob3 = item.innerText;
          count++;
        }
      }
    }
    if (count !== 0) {
      jobsQuery =
        "job1=" +
        selectedJob1 +
        "&job2=" +
        selectedJob2 +
        "&job3=" +
        selectedJob3;
      //   firstBool = true;
      //   for (let item of selectedJobsStr) {
      //     if (!firstBool) jobsQuery += "&";
      //     else firstBool = false;
      //     jobsQuery += "jobs=" + item;
      //   }
      location.href = "/reco/result/job?" + jobsQuery;
    } else {
      alert(
        "직무를 선택해주세요.\nPlease select a job.\n職務を選択してください。\nSeleziona un lavoro."
      );
    }
  });
  document.getElementById("searchSkillBtn").addEventListener("click", () => {
    selectedSkills = [];
    for (let item of selectedSkillObjs) {
      if (item.style.display === "grid") {
        skillId = String(item.id).replace("selectedSkill", "");
        selectedSkills.push(skillId);
      }
    }
    let firstSelectedText =
      firstOption.options[firstOption.selectedIndex].innerText;
    let secondSelectedText =
      secondOption.options[secondOption.selectedIndex].innerText;
    let thirdSelectedText =
      thirdOption.options[thirdOption.selectedIndex].innerText;
    let firstSelectedValue =
      firstOption.options[firstOption.selectedIndex].value;
    let secondSelectedValue =
      secondOption.options[secondOption.selectedIndex].value;
    let thirdSelectedValue =
      thirdOption.options[thirdOption.selectedIndex].value;
    if (selectedSkills.length !== 0) {
      skillsQuery = "";
      favorQuery = "";
      firstBool = true;
      for (let item of selectedSkills) {
        if (!firstBool) skillsQuery += "&";
        else firstBool = false;
        skillsQuery += "skills=" + item;
      }
      if (firstSelectedValue !== "")
        favorQuery += "&first=" + firstSelectedText;
      if (secondSelectedValue !== "")
        favorQuery += "&second=" + secondSelectedText;
      if (thirdSelectedValue !== "")
        favorQuery += "&third=" + thirdSelectedText;
      location.href = "/reco/result/skill?" + skillsQuery + favorQuery;
    } else {
      alert(
        "스킬을 선택해주세요.\nPlease select a skill.\n技術を選択してください。\nSeleziona un'abilità."
      );
    }
  });
  // 검색 관련 종료

  // 옵션 관련
  plusOption.addEventListener("click", () => {
    let firstOptions = firstOption.getElementsByTagName("option");
    let secondOptions = secondOption.getElementsByTagName("option");
    let thirdOptions = thirdOption.getElementsByTagName("option");
    firstOptions[0].selected = true;
    secondOptions[0].selected = true;
    thirdOptions[0].selected = true;
    document.getElementById("secondOptionBox").style.display = "none";
    document.getElementById("thirdOptionBox").style.display = "none";
    if (favorOptionContainer.style.display === "block") {
      favorOptionContainer.style.display = "none";
      plusOption.innerHTML = '<i class="fas fa-plus"></i>';
    } else {
      favorOptionContainer.style.display = "block";
      plusOption.innerHTML = '<i class="fas fa-minus"></i>';
    }
  });
  firstOption.addEventListener("change", (obj) => {
    let selectedValue = obj.target.options[obj.target.selectedIndex].value;
    document.getElementById("secondOptionBox").style.display = "grid";
    let secondOptions = secondOption.getElementsByTagName("option");
    let thirdOptions = thirdOption.getElementsByTagName("option");
    secondOptions[0].selected = true;
    thirdOptions[0].selected = true;
    document.getElementById("thirdOptionBox").style.display = "none";
    for (let opt of secondOptions) {
      if (opt.value === selectedValue) opt.hidden = true;
      else opt.hidden = false;
    }
    secondOptions[0].hidden = true;
    thirdOptions[0].hidden = true;
  });
  secondOption.addEventListener("change", (obj) => {
    let firstSelectedValue =
      firstOption.options[firstOption.selectedIndex].value;
    let selectedValue = obj.target.options[obj.target.selectedIndex].value;
    document.getElementById("thirdOptionBox").style.display = "grid";
    let thirdOptions = thirdOption.getElementsByTagName("option");
    thirdOptions[0].selected = true;
    for (let opt of thirdOptions) {
      if (opt.value === selectedValue || opt.value === firstSelectedValue)
        opt.hidden = true;
      else opt.hidden = false;
    }
    thirdOptions[0].hidden = true;
  });
  firstOption.addEventListener("change", (obj) => {
    let selectedValue = obj.target.options[obj.target.selectedIndex].value;
    document.getElementById("secondOptionBox").style.display = "grid";
    let secondOption = document.getElementById("secondOption");
    secondOption.style.display = "block";
    let secondOptions = secondOption.getElementsByTagName("option");
    for (let opt of secondOptions) {
      if (opt.value === selectedValue) {
        opt.hidden = true;
      }
    }
  });
  // 옵션 관련 종료
  skillLayer.addEventListener("click", (obj) => {
    if (obj.target.id === "skillLayer") skillLayer.style.display = "none";
  });
  jobLayer.addEventListener("click", (obj) => {
    if (obj.target.id === "jobLayer") jobLayer.style.display = "none";
  });
  skillBtn.addEventListener("click", () => {
    skillContainer.style.display = "block";
    jobContainer.style.display = "none";
    checkBtns();
  });
  jobBtn.addEventListener("click", () => {
    skillContainer.style.display = "none";
    jobContainer.style.display = "block";
    checkBtns();
  });
  document.getElementById("addSkillBtn").addEventListener("click", () => {
    skillLayer.style.display = "block";
    document.getElementById("categoryListLanguages").style.display = "block";
    checkSkillCategory();
    checkSelectedItem();
    countingSelectedSkillCount();
  });
  document.getElementById("addJobBtn").addEventListener("click", () => {
    jobLayer.style.display = "block";
    checkSelectedItemJob();
    countingSelectedJobCount();
  });
  document.getElementById("skillConfirm").addEventListener("click", () => {
    skillLayer.style.display = "none";
    categoryContainers = document.getElementsByClassName(
      "layer-item-container"
    );
    for (let cateCon of categoryContainers) {
      cateCon.style.display = "none";
    }
  });
  document.getElementById("jobConfirm").addEventListener("click", () => {
    jobLayer.style.display = "none";
  });
  for (let item of skillItems) {
    item.addEventListener("click", async (obj) => {
      func = async () => {
        if (obj.target.className === "skill-item selected-skill-option") {
          obj.target.className = "skill-item";
        } else {
          if (selectedSkillCount < 10)
            obj.target.className = "skill-item selected-skill-option";
        }
      };
      await func().then(() => {
        checkSelectedSkill();
      });
    });
  }
  for (let item of jobItems) {
    item.addEventListener("click", async (obj) => {
      func = async () => {
        if (obj.target.className === "job-item selected-job-option") {
          obj.target.className = "job-item";
        } else {
          if (selectedJobCount < 3)
            obj.target.className = "job-item selected-job-option";
        }
      };
      await func().then(() => {
        checkSelectedJob();
      });
    });
  }

  for (let item of selectedSkillObjs) {
    item.addEventListener("click", (obj) => {
      item.style.display = "none";
      checkSkillBox();
    });
  }

  for (let item of selectedJobObjs) {
    item.addEventListener("click", (obj) => {
      item.style.display = "none";
      checkJobBox();
    });
  }

  for (let item of categories) {
    item.addEventListener("click", (obj) => {
      categoryContainers = document.getElementsByClassName(
        "layer-item-container"
      );
      for (let cateCon of categoryContainers) {
        cateCon.style.display = "none";
      }
      targetId = "categoryList" + String(obj.target.id).replace("category", "");
      document.getElementById(targetId).style.display = "block";
      checkSkillCategory();
    });
  }

  // 체크 한 스킬 화면에 리스트화
  checkSelectedSkill = () => {
    skillOptions = document.getElementsByClassName("skill-item");
    for (let skillOption of skillOptions) {
      targetObj = document.getElementById(
        "selectedSkill" + String(skillOption.id).replace("item", "")
      );
      if (skillOption.className === "skill-item selected-skill-option") {
        targetObj.style.display = "grid";
      } else {
        targetObj.style.display = "none";
      }
    }
    checkSkillBox();
    countingSelectedSkillCount();
  };

  // 체크 한 직무 화면에 리스트화 Job
  checkSelectedJob = () => {
    jobOptions = document.getElementsByClassName("job-item");
    for (let jobOption of jobOptions) {
      targetObj = document.getElementById(
        "selectedJob" + String(jobOption.id).replace("jobItem", "")
      );
      if (jobOption.className === "job-item selected-job-option") {
        targetObj.style.display = "grid";
      } else {
        targetObj.style.display = "none";
      }
    }
    checkJobBox();
    countingSelectedJobCount();
  };

  countingSelectedSkillCount = () => {
    selectedSkillCount = 0;
    for (let item of selectedSkillObjs) {
      if (item.style.display === "grid") {
        selectedSkillCount++;
      }
    }
  };

  countingSelectedJobCount = () => {
    selectedJobCount = 0;
    for (let item of selectedJobObjs) {
      if (item.style.display === "grid") {
        selectedJobCount++;
      }
    }
  };

  // 화면에 display: grid인 값을 체크 해서 레이어에 출력
  checkSelectedItem = () => {
    for (let selectedSkillObj of selectedSkillObjs) {
      targetObj = document.getElementById(
        "item" + String(selectedSkillObj.id).replace("selectedSkill", "")
      );
      if (selectedSkillObj.style.display === "grid") {
        targetObj.className = "skill-item selected-skill-option";
      } else {
        targetObj.className = "skill-item";
      }
    }
  };

  // 화면에 display: grid인 값을 체크 해서 레이어에 출력 Job
  checkSelectedItemJob = () => {
    for (let selectedJobObj of selectedJobObjs) {
      targetObj = document.getElementById(
        "jobItem" + String(selectedJobObj.id).replace("selectedJob", "")
      );
      if (selectedJobObj.style.display === "grid") {
        targetObj.className = "job-item selected-job-option";
      } else {
        targetObj.className = "job-item";
      }
    }
  };

  checkSkillCategory = () => {
    categoryContainers = document.getElementsByClassName(
      "layer-item-container"
    );
    for (let cateCon of categoryContainers) {
      if (cateCon.style.display === "block") {
        targetId = String(cateCon.id).replace("List", "");
        targetObj = document.getElementById(targetId);
        targetObj.style.border = "1px solid rgba(0, 0, 0, 0.6)";
        targetObj.style.borderRight = "5px solid rgba(0, 0, 0, 0.6)";
      } else {
        targetId = String(cateCon.id).replace("List", "");
        targetObj = document.getElementById(targetId);
        targetObj.style.border = "";
        targetObj.style.borderRight = "";
      }
    }
  };

  checkSkillBox = () => {
    count = 0;
    for (let item of selectedSkillObjs) {
      if (item.style.display === "grid") count++;
    }
    skillNoitem = document.getElementById("skillNoitem");
    if (count === 0) {
      skillNoitem.style.display = "block";
    } else {
      skillNoitem.style.display = "none";
    }
  };

  checkJobBox = () => {
    count = 0;
    for (let item of selectedJobObjs) {
      if (item.style.display === "grid") count++;
    }
    jobNoitem = document.getElementById("jobNoitem");
    if (count === 0) {
      jobNoitem.style.display = "block";
    } else {
      jobNoitem.style.display = "none";
    }
  };

  checkBtns = () => {
    if (skillContainer.style.display === "block") {
      skillBtn.style.borderBottom = "3px solid #666";
      jobBtn.style.borderBottom = "0";
    } else if (jobContainer.style.display === "block") {
      skillBtn.style.borderBottom = "0";
      jobBtn.style.borderBottom = "3px solid #666";
    }
    checkSkillBox();
    checkJobBox();
  };
  checkBtns();
};
