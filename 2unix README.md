[1mdiff --git a/.editorconfig b/.editorconfig[m
[1mindex de6f04b..0e66cdf 100644[m
[1m--- a/.editorconfig[m
[1m+++ b/.editorconfig[m
[36m@@ -1,34 +1,34 @@[m
[31m-# http://editorconfig.org[m
[31m-[m
[31m-root = true[m
[31m-[m
[31m-[*][m
[31m-charset = utf-8[m
[31m-end_of_line = lf[m
[31m-insert_final_newline = true[m
[31m-trim_trailing_whitespace = true[m
[31m-[m
[31m-[*.{py,rst,ini}][m
[31m-indent_style = space[m
[31m-indent_size = 4[m
[31m-[m
[31m-[*.{html,css,scss,json,yml,xml}][m
[31m-indent_style = space[m
[31m-indent_size = 2[m
[31m-[m
[31m-[*.md][m
[31m-trim_trailing_whitespace = false[m
[31m-[m
[31m-[default.conf][m
[31m-indent_style = space[m
[31m-indent_size = 2[m
[31m-[m
[31m-["Makefile"][m
[31m-indent_style = tab[m
[31m-[m
[31m-[*.{diff,patch}][m
[31m-trim_trailing_whitespace = false[m
[31m-[m
[31m-[*.bat][m
[31m-indent_style = tab[m
[31m-end_of_line = crlf[m
[32m+[m[32m# http://editorconfig.org[m[41m[m
[32m+[m[41m[m
[32m+[m[32mroot = true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*][m[41m[m
[32m+[m[32mcharset = utf-8[m[41m[m
[32m+[m[32mend_of_line = lf[m[41m[m
[32m+[m[32minsert_final_newline = true[m[41m[m
[32m+[m[32mtrim_trailing_whitespace = true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*.{py,rst,ini}][m[41m[m
[32m+[m[32mindent_style = space[m[41m[m
[32m+[m[32mindent_size = 4[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*.{html,css,scss,json,yml,xml}][m[41m[m
[32m+[m[32mindent_style = space[m[41m[m
[32m+[m[32mindent_size = 2[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*.md][m[41m[m
[32m+[m[32mtrim_trailing_whitespace = false[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[default.conf][m[41m[m
[32m+[m[32mindent_style = space[m[41m[m
[32m+[m[32mindent_size = 2[m[41m[m
[32m+[m[41m[m
[32m+[m[32m["Makefile"][m[41m[m
[32m+[m[32mindent_style = tab[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*.{diff,patch}][m[41m[m
[32m+[m[32mtrim_trailing_whitespace = false[m[41m[m
[32m+[m[41m[m
[32m+[m[32m[*.bat][m[41m[m
[32m+[m[32mindent_style = tab[m[41m[m
[32m+[m[32mend_of_line = crlf[m[41m[m
[1mdiff --git a/.envs/.env.tpl b/.envs/.env.tpl[m
[1mindex b5921c6..c1e5d40 100644[m
[1m--- a/.envs/.env.tpl[m
[1m+++ b/.envs/.env.tpl[m
[36m@@ -1 +1 @@[m
[31m-OPENAI_API_KEY=${OPENAI_API_KEY}[m
[32m+[m[32mOPENAI_API_KEY=${OPENAI_API_KEY}[m[41m[m
[1mdiff --git a/.github/ISSUE_TEMPLATE/bug-report.yml b/.github/ISSUE_TEMPLATE/bug-report.yml[m
[1mindex 6ff474f..3f99bb2 100644[m
[1m--- a/.github/ISSUE_TEMPLATE/bug-report.yml[m
[1m+++ b/.github/ISSUE_TEMPLATE/bug-report.yml[m
[36m@@ -1,149 +1,149 @@[m
[31m----[m
[31m-name: 🐛  Bug Report[m
[31m-description: Create a report to help us improve[m
[31m-labels: ["bug", "needs-triage"][m
[31m-[m
[31m-body:[m
[31m-  - type: markdown[m
[31m-    attributes:[m
[31m-      value: >[m
[31m-        **Thank you for wanting to report a bug in hiperhealth!**[m
[31m-[m
[31m-[m
[31m-        ⚠[m
[31m-        Verify first that your issue is not [already reported on[m
[31m-        GitHub][issue search].[m
[31m-[m
[31m-[m
[31m-        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Abug[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Summary[m
[31m-      description: Explain the problem briefly below.[m
[31m-      placeholder: >-[m
[31m-        When I try to do X with {{ cookiecutter.project_name }} and the following workspace, Y breaks or[m
[31m-        Z happens in an unexpected manner.[m
[31m-        Here are all the details I know about this problem.[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: OS / Environment[m
[31m-      description: >-[m
[31m-        Provide information on your operating system.[m
[31m-        Something like the output of `cat /etc/os-release` on Linux or[m
[31m-        `system_profiler -detailLevel mini SPSoftwareDataType` on macOS.[m
[31m-      render: console[m
[31m-      placeholder: |[m
[31m-        # Linux[m
[31m-        $ cat /etc/os-release[m
[31m-        NAME="Ubuntu"[m
[31m-        VERSION="20.04.2 LTS (Focal Fossa)"[m
[31m-        ID=ubuntu[m
[31m-        ID_LIKE=debian[m
[31m-        PRETTY_NAME="Ubuntu 20.04.2 LTS"[m
[31m-        VERSION_ID="20.04"[m
[31m-        HOME_URL="https://www.ubuntu.com/"[m
[31m-        SUPPORT_URL="https://help.ubuntu.com/"[m
[31m-        BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"[m
[31m-        PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"[m
[31m-        VERSION_CODENAME=focal[m
[31m-        UBUNTU_CODENAME=focal[m
[31m-[m
[31m-        # macOS[m
[31m-        $ system_profiler -detailLevel mini SPSoftwareDataType | head -n 6[m
[31m-        Software:[m
[31m-[m
[31m-            System Software Overview:[m
[31m-[m
[31m-              System Version: macOS 10.15.7 (19H1323)[m
[31m-              Kernel Version: Darwin 19.6.0[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Steps to Reproduce[m
[31m-      description: >-[m
[31m-        Describe exactly how to reproduce the problem, using a minimal test-case.[m
[31m-        It would *really* help us understand your problem if you paste in the Python code[m
[31m-        that you're running.[m
[31m-[m
[31m-[m
[31m-        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m
[31m-      value: |[m
[31m-        <!--- Paste your minimal failing Python example code between the quotes below -->[m
[31m-        ```python (paste below)[m
[31m-[m
[31m-        ```[m
[31m-[m
[31m-        <!--- ...or if you have a failing CLI command paste it between the quotes below -->[m
[31m-        ```console (paste below)[m
[31m-[m
[31m-        ```[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: File Upload (optional)[m
[31m-      description: >-[m
[31m-        If your steps to reproduce your minimal failing example require either a spec or a[m
[31m-        workspace file, please upload it by attaching it to the text area here.[m
[31m-[m
[31m-[m
[31m-        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m
[31m-      placeholder: >-[m
[31m-        Attach any files or compressed archives by dragging & dropping, selecting,[m
[31m-        or pasting them here.[m
[31m-    validations:[m
[31m-      required: false[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Expected Results[m
[31m-      description: >-[m
[31m-        Describe what you expected to happen when running the steps above.[m
[31m-      placeholder: >-[m
[31m-        I expected X to happen because I assumed Y.[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Actual Results[m
[31m-      description: >-[m
[31m-        Paste verbatim program or command output.[m
[31m-        Don't wrap it with triple backticks &mdash; your whole input will be[m
[31m-        turned into a code snippet automatically.[m
[31m-      render: console[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      # label: hiperhealth version[m
[31m-      # description: >-[m
[31m-      # Paste verbatim output from `hiperhealth --version` below, under the prompt line.[m
[31m-      # Don't wrap it with triple backticks &mdash; your whole input will be[m
[31m-      # turned into a code snippet automatically.[m
[31m-      render: console[m
[31m-      placeholder: |[m
[31m-        python -m pip show hiperhealth[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: checkboxes[m
[31m-    attributes:[m
[31m-      label: Code of Conduct[m
[31m-      description: |[m
[31m-        Read the [`hiperhealth` Code of Conduct][CoC] first.[m
[31m-[m
[31m-        [CoC]: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m
[31m-      options:[m
[31m-        - label: I agree to follow the Code of Conduct[m
[31m-          required: true[m
[31m----[m
[31m-This template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mname: 🐛  Bug Report[m[41m[m
[32m+[m[32mdescription: Create a report to help us improve[m[41m[m
[32m+[m[32mlabels: ["bug", "needs-triage"][m[41m[m
[32m+[m[41m[m
[32m+[m[32mbody:[m[41m[m
[32m+[m[32m  - type: markdown[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      value: >[m[41m[m
[32m+[m[32m        **Thank you for wanting to report a bug in hiperhealth!**[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ⚠[m[41m[m
[32m+[m[32m        Verify first that your issue is not [already reported on[m[41m[m
[32m+[m[32m        GitHub][issue search].[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Abug[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Summary[m[41m[m
[32m+[m[32m      description: Explain the problem briefly below.[m[41m[m
[32m+[m[32m      placeholder: >-[m[41m[m
[32m+[m[32m        When I try to do X with {{ cookiecutter.project_name }} and the following workspace, Y breaks or[m[41m[m
[32m+[m[32m        Z happens in an unexpected manner.[m[41m[m
[32m+[m[32m        Here are all the details I know about this problem.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: OS / Environment[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        Provide information on your operating system.[m[41m[m
[32m+[m[32m        Something like the output of `cat /etc/os-release` on Linux or[m[41m[m
[32m+[m[32m        `system_profiler -detailLevel mini SPSoftwareDataType` on macOS.[m[41m[m
[32m+[m[32m      render: console[m[41m[m
[32m+[m[32m      placeholder: |[m[41m[m
[32m+[m[32m        # Linux[m[41m[m
[32m+[m[32m        $ cat /etc/os-release[m[41m[m
[32m+[m[32m        NAME="Ubuntu"[m[41m[m
[32m+[m[32m        VERSION="20.04.2 LTS (Focal Fossa)"[m[41m[m
[32m+[m[32m        ID=ubuntu[m[41m[m
[32m+[m[32m        ID_LIKE=debian[m[41m[m
[32m+[m[32m        PRETTY_NAME="Ubuntu 20.04.2 LTS"[m[41m[m
[32m+[m[32m        VERSION_ID="20.04"[m[41m[m
[32m+[m[32m        HOME_URL="https://www.ubuntu.com/"[m[41m[m
[32m+[m[32m        SUPPORT_URL="https://help.ubuntu.com/"[m[41m[m
[32m+[m[32m        BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"[m[41m[m
[32m+[m[32m        PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"[m[41m[m
[32m+[m[32m        VERSION_CODENAME=focal[m[41m[m
[32m+[m[32m        UBUNTU_CODENAME=focal[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        # macOS[m[41m[m
[32m+[m[32m        $ system_profiler -detailLevel mini SPSoftwareDataType | head -n 6[m[41m[m
[32m+[m[32m        Software:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m            System Software Overview:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m              System Version: macOS 10.15.7 (19H1323)[m[41m[m
[32m+[m[32m              Kernel Version: Darwin 19.6.0[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Steps to Reproduce[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        Describe exactly how to reproduce the problem, using a minimal test-case.[m[41m[m
[32m+[m[32m        It would *really* help us understand your problem if you paste in the Python code[m[41m[m
[32m+[m[32m        that you're running.[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m[41m[m
[32m+[m[32m      value: |[m[41m[m
[32m+[m[32m        <!--- Paste your minimal failing Python example code between the quotes below -->[m[41m[m
[32m+[m[32m        ```python (paste below)[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ```[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        <!--- ...or if you have a failing CLI command paste it between the quotes below -->[m[41m[m
[32m+[m[32m        ```console (paste below)[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ```[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: File Upload (optional)[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        If your steps to reproduce your minimal failing example require either a spec or a[m[41m[m
[32m+[m[32m        workspace file, please upload it by attaching it to the text area here.[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m[41m[m
[32m+[m[32m      placeholder: >-[m[41m[m
[32m+[m[32m        Attach any files or compressed archives by dragging & dropping, selecting,[m[41m[m
[32m+[m[32m        or pasting them here.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: false[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Expected Results[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        Describe what you expected to happen when running the steps above.[m[41m[m
[32m+[m[32m      placeholder: >-[m[41m[m
[32m+[m[32m        I expected X to happen because I assumed Y.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Actual Results[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        Paste verbatim program or command output.[m[41m[m
[32m+[m[32m        Don't wrap it with triple backticks &mdash; your whole input will be[m[41m[m
[32m+[m[32m        turned into a code snippet automatically.[m[41m[m
[32m+[m[32m      render: console[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      # label: hiperhealth version[m[41m[m
[32m+[m[32m      # description: >-[m[41m[m
[32m+[m[32m      # Paste verbatim output from `hiperhealth --version` below, under the prompt line.[m[41m[m
[32m+[m[32m      # Don't wrap it with triple backticks &mdash; your whole input will be[m[41m[m
[32m+[m[32m      # turned into a code snippet automatically.[m[41m[m
[32m+[m[32m      render: console[m[41m[m
[32m+[m[32m      placeholder: |[m[41m[m
[32m+[m[32m        python -m pip show hiperhealth[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: checkboxes[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Code of Conduct[m[41m[m
[32m+[m[32m      description: |[m[41m[m
[32m+[m[32m        Read the [`hiperhealth` Code of Conduct][CoC] first.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [CoC]: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m[41m[m
[32m+[m[32m      options:[m[41m[m
[32m+[m[32m        - label: I agree to follow the Code of Conduct[m[41m[m
[32m+[m[32m          required: true[m[41m[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mThis template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m[41m[m
[1mdiff --git a/.github/ISSUE_TEMPLATE/config.yml b/.github/ISSUE_TEMPLATE/config.yml[m
[1mindex 5a17d57..02de65d 100644[m
[1m--- a/.github/ISSUE_TEMPLATE/config.yml[m
[1m+++ b/.github/ISSUE_TEMPLATE/config.yml[m
[36m@@ -1,15 +1,15 @@[m
[31m-# Ref: https://help.github.com/en/github/building-a-strong-community/configuring-issue-templates-for-your-repository#configuring-the-template-chooser[m
[31m-blank_issues_enabled: true[m
[31m-contact_links:[m
[31m-  - name: 🙋  Usage Questions[m
[31m-    url: https://github.com/hiperhealth/hiperhealth/discussions[m
[31m-    about: |[m
[31m-      Use hiperhealth's GitHub Discussions to ask "How do I do X with hiperhealth?".[m
[31m-  - name: 📖  Tutorial[m
[31m-    url: https://github.com/hiperhealth/hiperhealth[m
[31m-    about: |[m
[31m-      The hiperhealth tutorial is continually updated and provides an in depth walkthrough[m
[31m-      of how to use the latest release of hiperhealth.[m
[31m-  - name: 📝  hiperhealth Code of Conduct[m
[31m-    url: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m
[31m-    about: Expectations for how people will interact with each other on hiperhealth's GitHub.[m
[32m+[m[32m# Ref: https://help.github.com/en/github/building-a-strong-community/configuring-issue-templates-for-your-repository#configuring-the-template-chooser[m[41m[m
[32m+[m[32mblank_issues_enabled: true[m[41m[m
[32m+[m[32mcontact_links:[m[41m[m
[32m+[m[32m  - name: 🙋  Usage Questions[m[41m[m
[32m+[m[32m    url: https://github.com/hiperhealth/hiperhealth/discussions[m[41m[m
[32m+[m[32m    about: |[m[41m[m
[32m+[m[32m      Use hiperhealth's GitHub Discussions to ask "How do I do X with hiperhealth?".[m[41m[m
[32m+[m[32m  - name: 📖  Tutorial[m[41m[m
[32m+[m[32m    url: https://github.com/hiperhealth/hiperhealth[m[41m[m
[32m+[m[32m    about: |[m[41m[m
[32m+[m[32m      The hiperhealth tutorial is continually updated and provides an in depth walkthrough[m[41m[m
[32m+[m[32m      of how to use the latest release of hiperhealth.[m[41m[m
[32m+[m[32m  - name: 📝  hiperhealth Code of Conduct[m[41m[m
[32m+[m[32m    url: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m[41m[m
[32m+[m[32m    about: Expectations for how people will interact with each other on hiperhealth's GitHub.[m[41m[m
[1mdiff --git a/.github/ISSUE_TEMPLATE/documentation-report.yml b/.github/ISSUE_TEMPLATE/documentation-report.yml[m
[1mindex 0b643e4..f098c33 100644[m
[1m--- a/.github/ISSUE_TEMPLATE/documentation-report.yml[m
[1m+++ b/.github/ISSUE_TEMPLATE/documentation-report.yml[m
[36m@@ -1,53 +1,53 @@[m
[31m----[m
[31m-name: 📝  Documentation Report[m
[31m-description: Create a report for problems with the docs[m
[31m-labels: ["docs", "needs-triage"][m
[31m-[m
[31m-body:[m
[31m-  - type: markdown[m
[31m-    attributes:[m
[31m-      value: >[m
[31m-        **Thank you for wanting to report a problem with hiperhealth's documentation!**[m
[31m-[m
[31m-[m
[31m-        ⚠[m
[31m-        Verify first that your issue is not [already reported on[m
[31m-        GitHub][issue search].[m
[31m-[m
[31m-[m
[31m-        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Adocs[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Summary[m
[31m-      description: >-[m
[31m-        Explain the problem briefly below, add suggestions to wording or structure.[m
[31m-        If there are external references that are related please link them here[m
[31m-        as well.[m
[31m-      placeholder: >-[m
[31m-        I was reading the hiperhealth documentation for hiperhealth version X and I'm having[m
[31m-        problems understanding Y.[m
[31m-        It would be very helpful if that got rephrased as Z.[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: input[m
[31m-    attributes:[m
[31m-      label: Documentation Page Link[m
[31m-      description: |[m
[31m-        Paste the link to the documentation webpage that you have a question on.[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: checkboxes[m
[31m-    attributes:[m
[31m-      label: Code of Conduct[m
[31m-      description: |[m
[31m-        Read the [`hiperhealth` Code of Conduct][CoC] first.[m
[31m-[m
[31m-        [CoC]: https://github.com/hiperhealth/hiperhealth/blob/main/CODE_OF_CONDUCT.md[m
[31m-      options:[m
[31m-        - label: I agree to follow the Code of Conduct[m
[31m-          required: true[m
[31m----[m
[31m-This template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mname: 📝  Documentation Report[m[41m[m
[32m+[m[32mdescription: Create a report for problems with the docs[m[41m[m
[32m+[m[32mlabels: ["docs", "needs-triage"][m[41m[m
[32m+[m[41m[m
[32m+[m[32mbody:[m[41m[m
[32m+[m[32m  - type: markdown[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      value: >[m[41m[m
[32m+[m[32m        **Thank you for wanting to report a problem with hiperhealth's documentation!**[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ⚠[m[41m[m
[32m+[m[32m        Verify first that your issue is not [already reported on[m[41m[m
[32m+[m[32m        GitHub][issue search].[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Adocs[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Summary[m[41m[m
[32m+[m[32m      description: >-[m[41m[m
[32m+[m[32m        Explain the problem briefly below, add suggestions to wording or structure.[m[41m[m
[32m+[m[32m        If there are external references that are related please link them here[m[41m[m
[32m+[m[32m        as well.[m[41m[m
[32m+[m[32m      placeholder: >-[m[41m[m
[32m+[m[32m        I was reading the hiperhealth documentation for hiperhealth version X and I'm having[m[41m[m
[32m+[m[32m        problems understanding Y.[m[41m[m
[32m+[m[32m        It would be very helpful if that got rephrased as Z.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: input[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Documentation Page Link[m[41m[m
[32m+[m[32m      description: |[m[41m[m
[32m+[m[32m        Paste the link to the documentation webpage that you have a question on.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: checkboxes[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Code of Conduct[m[41m[m
[32m+[m[32m      description: |[m[41m[m
[32m+[m[32m        Read the [`hiperhealth` Code of Conduct][CoC] first.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [CoC]: https://github.com/hiperhealth/hiperhealth/blob/main/CODE_OF_CONDUCT.md[m[41m[m
[32m+[m[32m      options:[m[41m[m
[32m+[m[32m        - label: I agree to follow the Code of Conduct[m[41m[m
[32m+[m[32m          required: true[m[41m[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mThis template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m[41m[m
[1mdiff --git a/.github/ISSUE_TEMPLATE/feature-request.yml b/.github/ISSUE_TEMPLATE/feature-request.yml[m
[1mindex b9bcd3c..0537c35 100644[m
[1m--- a/.github/ISSUE_TEMPLATE/feature-request.yml[m
[1m+++ b/.github/ISSUE_TEMPLATE/feature-request.yml[m
[36m@@ -1,80 +1,80 @@[m
[31m----[m
[31m-name: ✨  Feature Request[m
[31m-description: Suggest an idea for this project[m
[31m-labels: ["feat/enhancement ", "needs-triage"][m
[31m-[m
[31m-body:[m
[31m-  - type: markdown[m
[31m-    attributes:[m
[31m-      value: >[m
[31m-        **Thank you for wanting to suggest a feature for hiperhealth!**[m
[31m-[m
[31m-[m
[31m-        ⚠[m
[31m-        Verify first that your issue is not [already reported on[m
[31m-        GitHub][issue search].[m
[31m-        Make sure to check the closed issues as well as it may[m
[31m-        already be implemented in a development release.[m
[31m-[m
[31m-[m
[31m-        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Afeat%2Fenhancement[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Summary[m
[31m-      description: >[m
[31m-        Describe the new feature/improvement you would like briefly below.[m
[31m-[m
[31m-[m
[31m-        What's the problem this feature will solve?[m
[31m-        What are you trying to do, that you are unable to achieve[m
[31m-        with the **latest** release of hiperhealth?[m
[31m-[m
[31m-[m
[31m-        * Provide examples of real-world use cases that this would enable[m
[31m-        and how it solves the problem you described.[m
[31m-[m
[31m-        * How do you solve this now?[m
[31m-[m
[31m-        * Have you tried to work around the problem?[m
[31m-[m
[31m-        * Could there be a different approach to solving this issue?[m
[31m-[m
[31m-[m
[31m-        If there are external references or other GitHub Issues that are related[m
[31m-        please link them here as well.[m
[31m-      placeholder: >-[m
[31m-        I am trying to do X with hiperhealth version x.y.z and I think that implementing[m
[31m-        new feature Y would be very helpful for me and every other user because of Z.[m
[31m-    validations:[m
[31m-      required: true[m
[31m-[m
[31m-  - type: textarea[m
[31m-    attributes:[m
[31m-      label: Additional Information[m
[31m-      description: |[m
[31m-        If you can, describe how the feature would be used in a mock code example.[m
[31m-[m
[31m-        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m
[31m-      value: |[m
[31m-        <!--- Describe what you are showing in your example -->[m
[31m-[m
[31m-        <!--- and then paste your mock Python example code between the quotes below -->[m
[31m-        ```python (paste below)[m
[31m-[m
[31m-        ```[m
[31m-    validations:[m
[31m-      required: false[m
[31m-[m
[31m-  - type: checkboxes[m
[31m-    attributes:[m
[31m-      label: Code of Conduct[m
[31m-      description: |[m
[31m-        Read the [`hiperhealth` Code of Conduct][CoC] first.[m
[31m-[m
[31m-        [CoC]: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m
[31m-      options:[m
[31m-        - label: I agree to follow the Code of Conduct[m
[31m-          required: true[m
[31m----[m
[31m-This template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mname: ✨  Feature Request[m[41m[m
[32m+[m[32mdescription: Suggest an idea for this project[m[41m[m
[32m+[m[32mlabels: ["feat/enhancement ", "needs-triage"][m[41m[m
[32m+[m[41m[m
[32m+[m[32mbody:[m[41m[m
[32m+[m[32m  - type: markdown[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      value: >[m[41m[m
[32m+[m[32m        **Thank you for wanting to suggest a feature for hiperhealth!**[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ⚠[m[41m[m
[32m+[m[32m        Verify first that your issue is not [already reported on[m[41m[m
[32m+[m[32m        GitHub][issue search].[m[41m[m
[32m+[m[32m        Make sure to check the closed issues as well as it may[m[41m[m
[32m+[m[32m        already be implemented in a development release.[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [issue search]: https://github.com/hiperhealth/hiperhealth/issues?q=is%3Aopen+is%3Aissue+label%3Afeat%2Fenhancement[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Summary[m[41m[m
[32m+[m[32m      description: >[m[41m[m
[32m+[m[32m        Describe the new feature/improvement you would like briefly below.[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        What's the problem this feature will solve?[m[41m[m
[32m+[m[32m        What are you trying to do, that you are unable to achieve[m[41m[m
[32m+[m[32m        with the **latest** release of hiperhealth?[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        * Provide examples of real-world use cases that this would enable[m[41m[m
[32m+[m[32m        and how it solves the problem you described.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        * How do you solve this now?[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        * Have you tried to work around the problem?[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        * Could there be a different approach to solving this issue?[m[41m[m
[32m+[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        If there are external references or other GitHub Issues that are related[m[41m[m
[32m+[m[32m        please link them here as well.[m[41m[m
[32m+[m[32m      placeholder: >-[m[41m[m
[32m+[m[32m        I am trying to do X with hiperhealth version x.y.z and I think that implementing[m[41m[m
[32m+[m[32m        new feature Y would be very helpful for me and every other user because of Z.[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: textarea[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Additional Information[m[41m[m
[32m+[m[32m      description: |[m[41m[m
[32m+[m[32m        If you can, describe how the feature would be used in a mock code example.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        **HINT:** You can paste [GitHub Gist](https://gist.github.com) links for larger files.[m[41m[m
[32m+[m[32m      value: |[m[41m[m
[32m+[m[32m        <!--- Describe what you are showing in your example -->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        <!--- and then paste your mock Python example code between the quotes below -->[m[41m[m
[32m+[m[32m        ```python (paste below)[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        ```[m[41m[m
[32m+[m[32m    validations:[m[41m[m
[32m+[m[32m      required: false[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  - type: checkboxes[m[41m[m
[32m+[m[32m    attributes:[m[41m[m
[32m+[m[32m      label: Code of Conduct[m[41m[m
[32m+[m[32m      description: |[m[41m[m
[32m+[m[32m        Read the [`hiperhealth` Code of Conduct][CoC] first.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m        [CoC]: https://github.com/hiperhealth/hiperhealth/coc/CODE_OF_CONDUCT.md[m[41m[m
[32m+[m[32m      options:[m[41m[m
[32m+[m[32m        - label: I agree to follow the Code of Conduct[m[41m[m
[32m+[m[32m          required: true[m[41m[m
[32m+[m[32m---[m[41m[m
[32m+[m[32mThis template has been adopted from [pyhf](https://github.com/scikit-hep/pyhf/tree/main/.github/ISSUE_TEMPLATE)'s excellent bug report template.[m[41m[m
[1mdiff --git a/.github/PULL_REQUEST_TEMPLATE.md b/.github/PULL_REQUEST_TEMPLATE.md[m
[1mindex 230e7d8..ca000e8 100644[m
[1m--- a/.github/PULL_REQUEST_TEMPLATE.md[m
[1m+++ b/.github/PULL_REQUEST_TEMPLATE.md[m
[36m@@ -1,90 +1,90 @@[m
[31m-<!--[m
[31m-[m
[31m-### Notes for PR's Author[m
[31m-[m
[31m-- This repository uses an AI bot for reviews. Keep your PR in **Draft** while[m
[31m-  you work. When you’re ready for a review, change the status to **Ready for[m
[31m-  review** to trigger a new review round. If you make additional changes and[m
[31m-  don’t want to trigger the bot, switch the PR back to **Draft**.[m
[31m-- AI-bot comments may not always be accurate. Please review them critically and[m
[31m-  share your feedback; it helps us improve the tool.[m
[31m-- Avoid changing code that is unrelated to your proposal. Keep your PR as short[m
[31m-  as possible to increase the chances of a timely review. Large PRs may not be[m
[31m-  reviewed and may be closed.[m
[31m-- Don’t add unnecessary comments. Your code should be readable and[m
[31m-  self-documenting[m
[31m-  ([guidance](https://google.github.io/styleguide/cppguide.html#Comments)).[m
[31m-- Don’t change core features without prior discussion with the community. Use[m
[31m-  our Discord to discuss ideas, blockers, or issues[m
[31m-  (https://discord.gg/Nu4MdGj9jB).[m
[31m-- Do not include secrets (API keys, tokens, passwords), credentials, or[m
[31m-  sensitive data/PII in code, configs, logs, screenshots, or commit history. If[m
[31m-  something leaks, rotate the credentials immediately, invalidate the old key,[m
[31m-  and note it in the PR so maintainers can assist.[m
[31m-- Do not commit large binaries or generated artifacts. If large datasets are[m
[31m-  needed for tests, prefer small fixtures or programmatic downloads declared in[m
[31m-  makim.yaml (e.g., a task that fetches data at test time). If a large binary is[m
[31m-  unavoidable, discuss first and consider Git LFS.[m
[31m--->[m
[31m-[m
[31m-## Pull Request description[m
[31m-[m
[31m-<!-- Describe the purpose of your PR and the changes you have made. -->[m
[31m-[m
[31m-<!-- Which issue this PR aims to resolve or fix? E.g.:[m
[31m-Fixes #4[m
[31m--->[m
[31m-[m
[31m-## How to test these changes[m
[31m-[m
[31m-<!-- Example:[m
[31m-[m
[31m-* run `$ abc -p 1234`[m
[31m-* open the web browser with url localhost:1234[m
[31m-* ...[m
[31m--->[m
[31m-[m
[31m-- `...`[m
[31m-[m
[31m-<!-- Modify the options to suit your project. -->[m
[31m-[m
[31m-## Pull Request checklists[m
[31m-[m
[31m-This PR is a:[m
[31m-[m
[31m-- [ ] bug-fix[m
[31m-- [ ] new feature[m
[31m-- [ ] maintenance[m
[31m-[m
[31m-About this PR:[m
[31m-[m
[31m-- [ ] it includes tests.[m
[31m-- [ ] the tests are executed on CI.[m
[31m-- [ ] the tests generate log file(s) (path).[m
[31m-- [ ] pre-commit hooks were executed locally.[m
[31m-- [ ] this PR requires a project documentation update.[m
[31m-[m
[31m-Author's checklist:[m
[31m-[m
[31m-- [ ] I have reviewed the changes and it contains no misspelling.[m
[31m-- [ ] The code is well commented, especially in the parts that contain more[m
[31m-      complexity.[m
[31m-- [ ] New and old tests passed locally.[m
[31m-[m
[31m-## Additional information[m
[31m-[m
[31m-<!-- Add any screenshot that helps to show the changes proposed -->[m
[31m-[m
[31m-<!-- Add any other extra information that would help to understand the changes proposed by this PR -->[m
[31m-[m
[31m-## Reviewer's checklist[m
[31m-[m
[31m-Copy and paste this template for your review's note:[m
[31m-[m
[31m-```[m
[31m-## Reviewer's Checklist[m
[31m-[m
[31m-- [ ] I managed to reproduce the problem locally from the `main` branch[m
[31m-- [ ] I managed to test the new changes locally[m
[31m-- [ ] I confirm that the issues mentioned were fixed/resolved[m
[31m-```[m
[32m+[m[32m<!--[m[41m[m
[32m+[m[41m[m
[32m+[m[32m### Notes for PR's Author[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- This repository uses an AI bot for reviews. Keep your PR in **Draft** while[m[41m[m
[32m+[m[32m  you work. When you’re ready for a review, change the status to **Ready for[m[41m[m
[32m+[m[32m  review** to trigger a new review round. If you make additional changes and[m[41m[m
[32m+[m[32m  don’t want to trigger the bot, switch the PR back to **Draft**.[m[41m[m
[32m+[m[32m- AI-bot comments may not always be accurate. Please review them critically and[m[41m[m
[32m+[m[32m  share your feedback; it helps us improve the tool.[m[41m[m
[32m+[m[32m- Avoid changing code that is unrelated to your proposal. Keep your PR as short[m[41m[m
[32m+[m[32m  as possible to increase the chances of a timely review. Large PRs may not be[m[41m[m
[32m+[m[32m  reviewed and may be closed.[m[41m[m
[32m+[m[32m- Don’t add unnecessary comments. Your code should be readable and[m[41m[m
[32m+[m[32m  self-documenting[m[41m[m
[32m+[m[32m  ([guidance](https://google.github.io/styleguide/cppguide.html#Comments)).[m[41m[m
[32m+[m[32m- Don’t change core features without prior discussion with the community. Use[m[41m[m
[32m+[m[32m  our Discord to discuss ideas, blockers, or issues[m[41m[m
[32m+[m[32m  (https://discord.gg/Nu4MdGj9jB).[m[41m[m
[32m+[m[32m- Do not include secrets (API keys, tokens, passwords), credentials, or[m[41m[m
[32m+[m[32m  sensitive data/PII in code, configs, logs, screenshots, or commit history. If[m[41m[m
[32m+[m[32m  something leaks, rotate the credentials immediately, invalidate the old key,[m[41m[m
[32m+[m[32m  and note it in the PR so maintainers can assist.[m[41m[m
[32m+[m[32m- Do not commit large binaries or generated artifacts. If large datasets are[m[41m[m
[32m+[m[32m  needed for tests, prefer small fixtures or programmatic downloads declared in[m[41m[m
[32m+[m[32m  makim.yaml (e.g., a task that fetches data at test time). If a large binary is[m[41m[m
[32m+[m[32m  unavoidable, discuss first and consider Git LFS.[m[41m[m
[32m+[m[32m-->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Pull Request description[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Describe the purpose of your PR and the changes you have made. -->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Which issue this PR aims to resolve or fix? E.g.:[m[41m[m
[32m+[m[32mFixes #4[m[41m[m
[32m+[m[32m-->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## How to test these changes[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Example:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m* run `$ abc -p 1234`[m[41m[m
[32m+[m[32m* open the web browser with url localhost:1234[m[41m[m
[32m+[m[32m* ...[m[41m[m
[32m+[m[32m-->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- `...`[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Modify the options to suit your project. -->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Pull Request checklists[m[41m[m
[32m+[m[41m[m
[32m+[m[32mThis PR is a:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- [ ] bug-fix[m[41m[m
[32m+[m[32m- [ ] new feature[m[41m[m
[32m+[m[32m- [ ] maintenance[m[41m[m
[32m+[m[41m[m
[32m+[m[32mAbout this PR:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- [ ] it includes tests.[m[41m[m
[32m+[m[32m- [ ] the tests are executed on CI.[m[41m[m
[32m+[m[32m- [ ] the tests generate log file(s) (path).[m[41m[m
[32m+[m[32m- [ ] pre-commit hooks were executed locally.[m[41m[m
[32m+[m[32m- [ ] this PR requires a project documentation update.[m[41m[m
[32m+[m[41m[m
[32m+[m[32mAuthor's checklist:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- [ ] I have reviewed the changes and it contains no misspelling.[m[41m[m
[32m+[m[32m- [ ] The code is well commented, especially in the parts that contain more[m[41m[m
[32m+[m[32m      complexity.[m[41m[m
[32m+[m[32m- [ ] New and old tests passed locally.[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Additional information[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Add any screenshot that helps to show the changes proposed -->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m<!-- Add any other extra information that would help to understand the changes proposed by this PR -->[m[41m[m
[32m+[m[41m[m
[32m+[m[32m## Reviewer's checklist[m[41m[m
[32m+[m[41m[m
[32m+[m[32mCopy and paste this template for your review's note:[m[41m[m
[32m+[m[41m[m
[32m+[m[32m```[m[41m[m
[32m+[m[32m## Reviewer's Checklist[m[41m[m
[32m+[m[41m[m
[32m+[m[32m- [ ] I managed to reproduce the problem locally from the `main` branch[m[41m[m
[32m+[m[32m- [ ] I managed to test the new changes locally[m[41m[m
[32m+[m[32m- [ ] I confirm that the issues mentioned were fixed/resolved[m[41m[m
[32m+[m[32m```[m[41m[m
[1mdiff --git a/.github/workflows/docs.yaml b/.github/workflows/docs.yaml[m
[1mindex a4a13ff..af03f02 100644[m
[1m--- a/.github/workflows/docs.yaml[m
[1m+++ b/.github/workflows/docs.yaml[m
[36m@@ -1,47 +1,47 @@[m
[31m-name: Documentation[m
[31m-[m
[31m-on:[m
[31m-  workflow_dispatch:[m
[31m-  push:[m
[31m-    branches: [main][m
[31m-  pull_request:[m
[31m-    branches: [main][m
[31m-[m
[31m-env:[m
[31m-  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m
[31m-[m
[31m-jobs:[m
[31m-  gen-docs:[m
[31m-    runs-on: ubuntu-latest[m
[31m-    timeout-minutes: 15[m
[31m-[m
[31m-    defaults:[m
[31m-      run:[m
[31m-        shell: bash -l {0}[m
[31m-[m
[31m-    steps:[m
[31m-      - uses: actions/checkout@v5[m
[31m-[m
[31m-      - uses: conda-incubator/setup-miniconda@v3[m
[31m-        with:[m
[31m-          miniforge-version: latest[m
[31m-          environment-file: conda/dev.yaml[m
[31m-          channels: nodefaults,conda-forge[m
[31m-          activate-environment: hiperhealth[m
[31m-          auto-update-conda: true[m
[31m-          conda-solver: libmamba[m
[31m-          python-version: "3.10"[m
[31m-[m
[31m-      - name: Install deps[m
[31m-        run: |[m
[31m-          ./scripts/install-dev.sh[m
[31m-[m
[31m-      - name: Generate documentation with changes from semantic-release[m
[31m-        run: makim --verbose docs.build[m
[31m-[m
[31m-      - name: GitHub Pages action[m
[31m-        if: ${{ github.event_name == 'workflow_dispatch' }}[m
[31m-        uses: peaceiris/actions-gh-pages@v3.5.9[m
[31m-        with:[m
[31m-          github_token: ${{ secrets.GITHUB_TOKEN }}[m
[31m-          publish_dir: ./build/[m
[32m+[m[32mname: Documentation[m[41m[m
[32m+[m[41m[m
[32m+[m[32mon:[m[41m[m
[32m+[m[32m  workflow_dispatch:[m[41m[m
[32m+[m[32m  push:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[32m  pull_request:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[41m[m
[32m+[m[32menv:[m[41m[m
[32m+[m[32m  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m[41m[m
[32m+[m[41m[m
[32m+[m[32mjobs:[m[41m[m
[32m+[m[32m  gen-docs:[m[41m[m
[32m+[m[32m    runs-on: ubuntu-latest[m[41m[m
[32m+[m[32m    timeout-minutes: 15[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    defaults:[m[41m[m
[32m+[m[32m      run:[m[41m[m
[32m+[m[32m        shell: bash -l {0}[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    steps:[m[41m[m
[32m+[m[32m      - uses: actions/checkout@v5[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - uses: conda-incubator/setup-miniconda@v3[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          miniforge-version: latest[m[41m[m
[32m+[m[32m          environment-file: conda/dev.yaml[m[41m[m
[32m+[m[32m          channels: nodefaults,conda-forge[m[41m[m
[32m+[m[32m          activate-environment: hiperhealth[m[41m[m
[32m+[m[32m          auto-update-conda: true[m[41m[m
[32m+[m[32m          conda-solver: libmamba[m[41m[m
[32m+[m[32m          python-version: "3.10"[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Install deps[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          ./scripts/install-dev.sh[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Generate documentation with changes from semantic-release[m[41m[m
[32m+[m[32m        run: makim --verbose docs.build[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: GitHub Pages action[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'workflow_dispatch' }}[m[41m[m
[32m+[m[32m        uses: peaceiris/actions-gh-pages@v3.5.9[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          github_token: ${{ secrets.GITHUB_TOKEN }}[m[41m[m
[32m+[m[32m          publish_dir: ./build/[m[41m[m
[1mdiff --git a/.github/workflows/main.yaml b/.github/workflows/main.yaml[m
[1mindex c3170ad..0ebb27c 100644[m
[1m--- a/.github/workflows/main.yaml[m
[1m+++ b/.github/workflows/main.yaml[m
[36m@@ -1,135 +1,135 @@[m
[31m-name: build[m
[31m-[m
[31m-on:[m
[31m-  push:[m
[31m-    branches: [main][m
[31m-  pull_request:[m
[31m-    branches: [main][m
[31m-[m
[31m-jobs:[m
[31m-  check-branch:[m
[31m-    runs-on: ubuntu-latest[m
[31m-[m
[31m-    timeout-minutes: 2[m
[31m-    concurrency:[m
[31m-      group: ci-check-branch-${{ github.ref }}[m
[31m-      cancel-in-progress: true[m
[31m-[m
[31m-    steps:[m
[31m-      - uses: actions/checkout@v4[m
[31m-        if: ${{ github.event_name == 'pull_request' }}[m
[31m-        with:[m
[31m-          fetch-depth: 0[m
[31m-[m
[31m-      - name: Check if the PR's branch is updated[m
[31m-        if: ${{ github.event_name == 'pull_request' }}[m
[31m-        uses: osl-incubator/gh-check-pr-is-updated@1.0.0[m
[31m-        with:[m
[31m-          remote_branch: origin/main[m
[31m-          pr_sha: ${{ github.event.pull_request.head.sha }}[m
[31m-[m
[31m-  tests:[m
[31m-    strategy:[m
[31m-      fail-fast: false[m
[31m-      matrix:[m
[31m-        python_version:[m
[31m-          - "3.10"[m
[31m-          - "3.11"[m
[31m-          - "3.12"[m
[31m-          - "3.13"[m
[31m-        os:[m
[31m-          - "ubuntu"[m
[31m-          - "macos"[m
[31m-          # - "windows"[m
[31m-[m
[31m-    runs-on: ${{ matrix.os }}-latest[m
[31m-    timeout-minutes: 20[m
[31m-[m
[31m-    defaults:[m
[31m-      run:[m
[31m-        shell: bash -l {0}[m
[31m-[m
[31m-    concurrency:[m
[31m-      group: ci-tests-${{ matrix.os }}-${{ matrix.python_version }}-${{ github.ref }}[m
[31m-      cancel-in-progress: true[m
[31m-[m
[31m-    steps:[m
[31m-      - uses: actions/checkout@v4[m
[31m-[m
[31m-      - uses: conda-incubator/setup-miniconda@v3[m
[31m-        if: ${{ matrix.os != 'windows' }}[m
[31m-        with:[m
[31m-          miniforge-version: latest[m
[31m-          environment-file: conda/dev.yaml[m
[31m-          channels: nodefaults,conda-forge[m
[31m-          activate-environment: hiperhealth[m
[31m-          auto-update-conda: true[m
[31m-          conda-solver: libmamba[m
[31m-          python-version: "${{ matrix.python_version }}"[m
[31m-[m
[31m-      - uses: conda-incubator/setup-miniconda@v3[m
[31m-        if: ${{ matrix.os == 'windows' }}[m
[31m-        with:[m
[31m-          miniforge-version: latest[m
[31m-          environment-file: conda/dev-win.yaml[m
[31m-          channels: nodefaults,conda-forge[m
[31m-          activate-environment: hiperhealth[m
[31m-          auto-update-conda: true[m
[31m-          conda-solver: libmamba[m
[31m-          python-version: "${{ matrix.python_version }}"[m
[31m-[m
[31m-      - name: Install dependencies[m
[31m-        run: |[m
[31m-          ./scripts/install-dev.sh[m
[31m-[m
[31m-      - name: Run unit tests[m
[31m-        run: makim tests.unit[m
[31m-[m
[31m-      - name: Semantic Release PR Title Check[m
[31m-        uses: osl-incubator/semantic-release-pr-title-check@v1.4.1[m
[31m-        if: success() || failure()[m
[31m-        with:[m
[31m-          convention-name: conventionalcommits[m
[31m-[m
[31m-      - name: Setup tmate session[m
[31m-        if: "${{ failure() && (contains(github.event.pull_request.labels.*.name, 'ci:enable-debugging')) }}"[m
[31m-        uses: mxschmitt/action-tmate@v3[m
[31m-[m
[31m-  linter:[m
[31m-    runs-on: ubuntu-latest[m
[31m-    timeout-minutes: 10[m
[31m-[m
[31m-    defaults:[m
[31m-      run:[m
[31m-        shell: bash -l {0}[m
[31m-[m
[31m-    concurrency:[m
[31m-      group: ci-linter-docs-${{ github.ref }}[m
[31m-      cancel-in-progress: true[m
[31m-[m
[31m-    steps:[m
[31m-      - uses: actions/checkout@v4[m
[31m-[m
[31m-      - uses: conda-incubator/setup-miniconda@v3[m
[31m-        with:[m
[31m-          miniforge-version: latest[m
[31m-          environment-file: conda/dev.yaml[m
[31m-          channels: nodefaults,conda-forge[m
[31m-          activate-environment: hiperhealth[m
[31m-          auto-update-conda: true[m
[31m-          conda-solver: libmamba[m
[31m-          python-version: "3.10"[m
[31m-[m
[31m-      - name: Install dependencies[m
[31m-        run: |[m
[31m-          ./scripts/install-dev.sh[m
[31m-[m
[31m-      - name: Run style checks[m
[31m-        if: success() || failure()[m
[31m-        run: |[m
[31m-          pre-commit install[m
[31m-          makim tests.linter[m
[31m-[m
[31m-      - name: Setup tmate session[m
[31m-        if: "${{ failure() && (contains(github.event.pull_request.labels.*.name, 'ci:enable-debugging')) }}"[m
[31m-        uses: mxschmitt/action-tmate@v3[m
[32m+[m[32mname: build[m[41m[m
[32m+[m[41m[m
[32m+[m[32mon:[m[41m[m
[32m+[m[32m  push:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[32m  pull_request:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[41m[m
[32m+[m[32mjobs:[m[41m[m
[32m+[m[32m  check-branch:[m[41m[m
[32m+[m[32m    runs-on: ubuntu-latest[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    timeout-minutes: 2[m[41m[m
[32m+[m[32m    concurrency:[m[41m[m
[32m+[m[32m      group: ci-check-branch-${{ github.ref }}[m[41m[m
[32m+[m[32m      cancel-in-progress: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    steps:[m[41m[m
[32m+[m[32m      - uses: actions/checkout@v4[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'pull_request' }}[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          fetch-depth: 0[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Check if the PR's branch is updated[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'pull_request' }}[m[41m[m
[32m+[m[32m        uses: osl-incubator/gh-check-pr-is-updated@1.0.0[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          remote_branch: origin/main[m[41m[m
[32m+[m[32m          pr_sha: ${{ github.event.pull_request.head.sha }}[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  tests:[m[41m[m
[32m+[m[32m    strategy:[m[41m[m
[32m+[m[32m      fail-fast: false[m[41m[m
[32m+[m[32m      matrix:[m[41m[m
[32m+[m[32m        python_version:[m[41m[m
[32m+[m[32m          - "3.10"[m[41m[m
[32m+[m[32m          - "3.11"[m[41m[m
[32m+[m[32m          - "3.12"[m[41m[m
[32m+[m[32m          - "3.13"[m[41m[m
[32m+[m[32m        os:[m[41m[m
[32m+[m[32m          - "ubuntu"[m[41m[m
[32m+[m[32m          - "macos"[m[41m[m
[32m+[m[32m          # - "windows"[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    runs-on: ${{ matrix.os }}-latest[m[41m[m
[32m+[m[32m    timeout-minutes: 20[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    defaults:[m[41m[m
[32m+[m[32m      run:[m[41m[m
[32m+[m[32m        shell: bash -l {0}[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    concurrency:[m[41m[m
[32m+[m[32m      group: ci-tests-${{ matrix.os }}-${{ matrix.python_version }}-${{ github.ref }}[m[41m[m
[32m+[m[32m      cancel-in-progress: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    steps:[m[41m[m
[32m+[m[32m      - uses: actions/checkout@v4[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - uses: conda-incubator/setup-miniconda@v3[m[41m[m
[32m+[m[32m        if: ${{ matrix.os != 'windows' }}[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          miniforge-version: latest[m[41m[m
[32m+[m[32m          environment-file: conda/dev.yaml[m[41m[m
[32m+[m[32m          channels: nodefaults,conda-forge[m[41m[m
[32m+[m[32m          activate-environment: hiperhealth[m[41m[m
[32m+[m[32m          auto-update-conda: true[m[41m[m
[32m+[m[32m          conda-solver: libmamba[m[41m[m
[32m+[m[32m          python-version: "${{ matrix.python_version }}"[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - uses: conda-incubator/setup-miniconda@v3[m[41m[m
[32m+[m[32m        if: ${{ matrix.os == 'windows' }}[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          miniforge-version: latest[m[41m[m
[32m+[m[32m          environment-file: conda/dev-win.yaml[m[41m[m
[32m+[m[32m          channels: nodefaults,conda-forge[m[41m[m
[32m+[m[32m          activate-environment: hiperhealth[m[41m[m
[32m+[m[32m          auto-update-conda: true[m[41m[m
[32m+[m[32m          conda-solver: libmamba[m[41m[m
[32m+[m[32m          python-version: "${{ matrix.python_version }}"[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Install dependencies[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          ./scripts/install-dev.sh[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Run unit tests[m[41m[m
[32m+[m[32m        run: makim tests.unit[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Semantic Release PR Title Check[m[41m[m
[32m+[m[32m        uses: osl-incubator/semantic-release-pr-title-check@v1.4.1[m[41m[m
[32m+[m[32m        if: success() || failure()[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          convention-name: conventionalcommits[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Setup tmate session[m[41m[m
[32m+[m[32m        if: "${{ failure() && (contains(github.event.pull_request.labels.*.name, 'ci:enable-debugging')) }}"[m[41m[m
[32m+[m[32m        uses: mxschmitt/action-tmate@v3[m[41m[m
[32m+[m[41m[m
[32m+[m[32m  linter:[m[41m[m
[32m+[m[32m    runs-on: ubuntu-latest[m[41m[m
[32m+[m[32m    timeout-minutes: 10[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    defaults:[m[41m[m
[32m+[m[32m      run:[m[41m[m
[32m+[m[32m        shell: bash -l {0}[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    concurrency:[m[41m[m
[32m+[m[32m      group: ci-linter-docs-${{ github.ref }}[m[41m[m
[32m+[m[32m      cancel-in-progress: true[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    steps:[m[41m[m
[32m+[m[32m      - uses: actions/checkout@v4[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - uses: conda-incubator/setup-miniconda@v3[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          miniforge-version: latest[m[41m[m
[32m+[m[32m          environment-file: conda/dev.yaml[m[41m[m
[32m+[m[32m          channels: nodefaults,conda-forge[m[41m[m
[32m+[m[32m          activate-environment: hiperhealth[m[41m[m
[32m+[m[32m          auto-update-conda: true[m[41m[m
[32m+[m[32m          conda-solver: libmamba[m[41m[m
[32m+[m[32m          python-version: "3.10"[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Install dependencies[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          ./scripts/install-dev.sh[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Run style checks[m[41m[m
[32m+[m[32m        if: success() || failure()[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          pre-commit install[m[41m[m
[32m+[m[32m          makim tests.linter[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Setup tmate session[m[41m[m
[32m+[m[32m        if: "${{ failure() && (contains(github.event.pull_request.labels.*.name, 'ci:enable-debugging')) }}"[m[41m[m
[32m+[m[32m        uses: mxschmitt/action-tmate@v3[m[41m[m
[1mdiff --git a/.github/workflows/release.yaml b/.github/workflows/release.yaml[m
[1mindex 3c23ca9..1dd4c98 100644[m
[1m--- a/.github/workflows/release.yaml[m
[1m+++ b/.github/workflows/release.yaml[m
[36m@@ -1,67 +1,67 @@[m
[31m-name: Release[m
[31m-[m
[31m-on:[m
[31m-  workflow_dispatch:[m
[31m-  push:[m
[31m-    branches: [main][m
[31m-  pull_request:[m
[31m-    branches: [main][m
[31m-[m
[31m-permissions:[m
[31m-  contents: write[m
[31m-  issues: write[m
[31m-  pull-requests: write[m
[31m-[m
[31m-jobs:[m
[31m-  release:[m
[31m-    name: Release[m
[31m-    runs-on: ubuntu-latest[m
[31m-    timeout-minutes: 10[m
[31m-[m
[31m-    defaults:[m
[31m-      run:[m
[31m-        shell: bash -l {0}[m
[31m-[m
[31m-    steps:[m
[31m-      - uses: actions/checkout@v4[m
[31m-[m
[31m-      - uses: conda-incubator/setup-miniconda@v3[m
[31m-        with:[m
[31m-          miniforge-version: latest[m
[31m-          environment-file: conda/dev.yaml[m
[31m-          channels: nodefaults,conda-forge[m
[31m-          activate-environment: hiperhealth[m
[31m-          auto-update-conda: true[m
[31m-          conda-solver: libmamba[m
[31m-[m
[31m-      - name: Install deps[m
[31m-        run: |[m
[31m-          ./scripts/install-dev.sh[m
[31m-[m
[31m-      - name: Run semantic release (for tests)[m
[31m-        if: ${{ github.event_name != 'workflow_dispatch' }}[m
[31m-        env:[m
[31m-          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m
[31m-        run: |[m
[31m-          makim release.dry[m
[31m-[m
[31m-      - name: Release command[m
[31m-        if: ${{ github.event_name == 'workflow_dispatch' }}[m
[31m-        env:[m
[31m-          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m
[31m-          PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}[m
[31m-        run: |[m
[31m-          makim release.ci[m
[31m-[m
[31m-      - name: Generate documentation with changes from semantic-release[m
[31m-        if: ${{ github.event_name == 'workflow_dispatch' }}[m
[31m-        run: |[m
[31m-          makim docs.build[m
[31m-[m
[31m-      - name: GitHub Pages action[m
[31m-        if: ${{ github.event_name == 'workflow_dispatch' }}[m
[31m-        uses: peaceiris/actions-gh-pages@v3.5.9[m
[31m-        with:[m
[31m-          github_token: ${{ secrets.GITHUB_TOKEN }}[m
[31m-          publish_dir: >-[m
[31m-            build/[m
[32m+[m[32mname: Release[m[41m[m
[32m+[m[41m[m
[32m+[m[32mon:[m[41m[m
[32m+[m[32m  workflow_dispatch:[m[41m[m
[32m+[m[32m  push:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[32m  pull_request:[m[41m[m
[32m+[m[32m    branches: [main][m[41m[m
[32m+[m[41m[m
[32m+[m[32mpermissions:[m[41m[m
[32m+[m[32m  contents: write[m[41m[m
[32m+[m[32m  issues: write[m[41m[m
[32m+[m[32m  pull-requests: write[m[41m[m
[32m+[m[41m[m
[32m+[m[32mjobs:[m[41m[m
[32m+[m[32m  release:[m[41m[m
[32m+[m[32m    name: Release[m[41m[m
[32m+[m[32m    runs-on: ubuntu-latest[m[41m[m
[32m+[m[32m    timeout-minutes: 10[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    defaults:[m[41m[m
[32m+[m[32m      run:[m[41m[m
[32m+[m[32m        shell: bash -l {0}[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    steps:[m[41m[m
[32m+[m[32m      - uses: actions/checkout@v4[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - uses: conda-incubator/setup-miniconda@v3[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          miniforge-version: latest[m[41m[m
[32m+[m[32m          environment-file: conda/dev.yaml[m[41m[m
[32m+[m[32m          channels: nodefaults,conda-forge[m[41m[m
[32m+[m[32m          activate-environment: hiperhealth[m[41m[m
[32m+[m[32m          auto-update-conda: true[m[41m[m
[32m+[m[32m          conda-solver: libmamba[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Install deps[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          ./scripts/install-dev.sh[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Run semantic release (for tests)[m[41m[m
[32m+[m[32m        if: ${{ github.event_name != 'workflow_dispatch' }}[m[41m[m
[32m+[m[32m        env:[m[41m[m
[32m+[m[32m          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          makim release.dry[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Release command[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'workflow_dispatch' }}[m[41m[m
[32m+[m[32m        env:[m[41m[m
[32m+[m[32m          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}[m[41m[m
[32m+[m[32m          PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          makim release.ci[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: Generate documentation with changes from semantic-release[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'workflow_dispatch' }}[m[41m[m
[32m+[m[32m        run: |[m[41m[m
[32m+[m[32m          makim docs.build[m[41m[m
[32m+[m[41m[m
[32m+[m[32m      - name: GitHub Pages action[m[41m[m
[32m+[m[32m        if: ${{ github.event_name == 'workflow_dispatch' }}[m[41m[m
[32m+[m[32m        uses: peaceiris/actions-gh-pages@v3.5.9[m[41m[m
[32m+[m[32m        with:[m[41m[m
[32m+[m[32m          github_token: ${{ secrets.GITHUB_TOKEN }}[m[41m[m
[32m+[m[32m          publish_dir: >-[m[41m[m
[32m+[m[32m            build/[m[41m[m
[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex 61bebca..81e6ba1 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -1,154 +1,154 @@[m
[31m-# Byte-compiled / optimized / DLL files[m
[31m-__pycache__/[m
[31m-*.py[cod][m
[31m-*$py.class[m
[31m-[m
[31m-# C extensions[m
[31m-*.so[m
[31m-[m
[31m-# Distribution / packaging[m
[31m-.Python[m
[31m-build/[m
[31m-develop-eggs/[m
[31m-dist/[m
[31m-downloads/[m
[31m-eggs/[m
[31m-.eggs/[m
[31m-lib/[m
[31m-lib64/[m
[31m-parts/[m
[31m-sdist/[m
[31m-var/[m
[31m-wheels/[m
[31m-share/python-wheels/[m
[31m-*.egg-info/[m
[31m-.installed.cfg[m
[31m-*.egg[m
[31m-MANIFEST[m
[31m-[m
[31m-# PyInstaller[m
[31m-#  Usually these files are written by a python script from a template[m
[31m-#  before PyInstaller builds the exe, so as to inject date/other infos into it.[m
[31m-*.manifest[m
[31m-*.spec[m
[31m-[m
[31m-# Installer logs[m
[31m-pip-log.txt[m
[31m-pip-delete-this-directory.txt[m
[31m-[m
[31m-# Unit test / coverage reports[m
[31m-htmlcov/[m
[31m-.tox/[m
[31m-.nox/[m
[31m-.coverage[m
[31m-.coverage.*[m
[31m-.cache[m
[31m-nosetests.xml[m
[31m-coverage.xml[m
[31m-*.cover[m
[31m-*.py,cover[m
[31m-.hypothesis/[m
[31m-.pytest_cache/[m
[31m-cover/[m
[31m-[m
[31m-# Translations[m
[31m-*.mo[m
[31m-*.pot[m
[31m-[m
[31m-# Django stuff:[m
[31m-*.log[m
[31m-local_settings.py[m
[31m-db.sqlite3[m
[31m-db.sqlite3-journal[m
[31m-db.sqlite[m
[31m-[m
[31m-# Flask stuff:[m
[31m-instance/[m
[31m-.webassets-cache[m
[31m-[m
[31m-# Scrapy stuff:[m
[31m-.scrapy[m
[31m-[m
[31m-# Sphinx documentation[m
[31m-docs/_build/[m
[31m-[m
[31m-# PyBuilder[m
[31m-.pybuilder/[m
[31m-target/[m
[31m-[m
[31m-# Jupyter Notebook[m
[31m-.ipynb_checkpoints[m
[31m-[m
[31m-# IPython[m
[31m-profile_default/[m
[31m-ipython_config.py[m
[31m-[m
[31m-# pyenv[m
[31m-#   For a library or package, you might want to ignore these files since the code is[m
[31m-#   intended to run in multiple environments; otherwise, check them in:[m
[31m-# .python-version[m
[31m-[m
[31m-# pipenv[m
[31m-#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.[m
[31m-#   However, in case of collaboration, if having platform-specific dependencies or dependencies[m
[31m-#   having no cross-platform support, pipenv may install dependencies that don't work, or not[m
[31m-#   install all needed dependencies.[m
[31m-#Pipfile.lock[m
[31m-[m
[31m-# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm[m
[31m-__pypackages__/[m
[31m-[m
[31m-# Celery stuff[m
[31m-celerybeat-schedule[m
[31m-celerybeat.pid[m
[31m-[m
[31m-# SageMath parsed files[m
[31m-*.sage.py[m
[31m-[m
[31m-# Environments[m
[31m-.env[m
[31m-.venv[m
[31m-env/[m
[31m-venv/[m
[31m-ENV/[m
[31m-env.bak/[m
[31m-venv.bak/[m
[31m-[m
[31m-# Spyder project settings[m
[31m-.spyderproject[m
[31m-.spyproject[m
[31m-[m
[31m-# Rope project settings[m
[31m-.ropeproject[m
[31m-[m
[31m-# mkdocs documentation[m
[31m-/site[m
[31m-[m
[31m-# mypy[m
[31m-.mypy_cache/[m
[31m-.dmypy.json[m
[31m-dmypy.json[m
[31m-[m
[31m-# Pyre type checker[m
[31m-.pyre/[m
[31m-[m
[31m-# pytype static type analyzer[m
[31m-.pytype/[m
[31m-[m
[31m-# Cython debug symbols[m
[31m-cython_debug/[m
[31m-[m
[31m-# PyCharm[m
[31m-#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can[m
[31m-#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore[m
[31m-#  and can be added to the global gitignore or merged into this file.  For a more nuclear[m
[31m-#  option (not recommended) you can uncomment the following to ignore the entire idea folder.[m
[31m-#.idea/[m
[31m-[m
[31m-# vscode[m
[31m-.vscode/[m
[31m-research/backend/data[m
[31m-#backend database[m
[31m-research-poc/backend/backend.db[m
[31m-uvicorn.log[m
[31m-uvicorn.pid[m
[32m+[m[32m# Byte-compiled / optimized / DLL files[m[41m[m
[32m+[m[32m__pycache__/[m[41m[m
[32m+[m[32m*.py[cod][m[41m[m
[32m+[m[32m*$py.class[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# C extensions[m[41m[m
[32m+[m[32m*.so[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Distribution / packaging[m[41m[m
[32m+[m[32m.Python[m[41m[m
[32m+[m[32mbuild/[m[41m[m
[32m+[m[32mdevelop-eggs/[m[41m[m
[32m+[m[32mdist/[m[41m[m
[32m+[m[32mdownloads/[m[41m[m
[32m+[m[32meggs/[m[41m[m
[32m+[m[32m.eggs/[m[41m[m
[32m+[m[32mlib/[m[41m[m
[32m+[m[32mlib64/[m[41m[m
[32m+[m[32mparts/[m[41m[m
[32m+[m[32msdist/[m[41m[m
[32m+[m[32mvar/[m[41m[m
[32m+[m[32mwheels/[m[41m[m
[32m+[m[32mshare/python-wheels/[m[41m[m
[32m+[m[32m*.egg-info/[m[41m[m
[32m+[m[32m.installed.cfg[m[41m[m
[32m+[m[32m*.egg[m[41m[m
[32m+[m[32mMANIFEST[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# PyInstaller[m[41m[m
[32m+[m[32m#  Usually these files are written by a python script from a template[m[41m[m
[32m+[m[32m#  before PyInstaller builds the exe, so as to inject date/other infos into it.[m[41m[m
[32m+[m[32m*.manifest[m[41m[m
[32m+[m[32m*.spec[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Installer logs[m[41m[m
[32m+[m[32mpip-log.txt[m[41m[m
[32m+[m[32mpip-delete-this-directory.txt[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Unit test / coverage reports[m[41m[m
[32m+[m[32mhtmlcov/[m[41m[m
[32m+[m[32m.tox/[m[41m[m
[32m+[m[32m.nox/[m[41m[m
[32m+[m[32m.coverage[m[41m[m
[32m+[m[32m.coverage.*[m[41m[m
[32m+[m[32m.cache[m[41m[m
[32m+[m[32mnosetests.xml[m[41m[m
[32m+[m[32mcoverage.xml[m[41m[m
[32m+[m[32m*.cover[m[41m[m
[32m+[m[32m*.py,cover[m[41m[m
[32m+[m[32m.hypothesis/[m[41m[m
[32m+[m[32m.pytest_cache/[m[41m[m
[32m+[m[32mcover/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Translations[m[41m[m
[32m+[m[32m*.mo[m[41m[m
[32m+[m[32m*.pot[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Django stuff:[m[41m[m
[32m+[m[32m*.log[m[41m[m
[32m+[m[32mlocal_settings.py[m[41m[m
[32m+[m[32mdb.sqlite3[m[41m[m
[32m+[m[32mdb.sqlite3-journal[m[41m[m
[32m+[m[32mdb.sqlite[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Flask stuff:[m[41m[m
[32m+[m[32minstance/[m[41m[m
[32m+[m[32m.webassets-cache[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Scrapy stuff:[m[41m[m
[32m+[m[32m.scrapy[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Sphinx documentation[m[41m[m
[32m+[m[32mdocs/_build/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# PyBuilder[m[41m[m
[32m+[m[32m.pybuilder/[m[41m[m
[32m+[m[32mtarget/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Jupyter Notebook[m[41m[m
[32m+[m[32m.ipynb_checkpoints[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# IPython[m[41m[m
[32m+[m[32mprofile_default/[m[41m[m
[32m+[m[32mipython_config.py[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# pyenv[m[41m[m
[32m+[m[32m#   For a library or package, you might want to ignore these files since the code is[m[41m[m
[32m+[m[32m#   intended to run in multiple environments; otherwise, check them in:[m[41m[m
[32m+[m[32m# .python-version[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# pipenv[m[41m[m
[32m+[m[32m#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.[m[41m[m
[32m+[m[32m#   However, in case of collaboration, if having platform-specific dependencies or dependencies[m[41m[m
[32m+[m[32m#   having no cross-platform support, pipenv may install dependencies that don't work, or not[m[41m[m
[32m+[m[32m#   install all needed dependencies.[m[41m[m
[32m+[m[32m#Pipfile.lock[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm[m[41m[m
[32m+[m[32m__pypackages__/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Celery stuff[m[41m[m
[32m+[m[32mcelerybeat-schedule[m[41m[m
[32m+[m[32mcelerybeat.pid[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# SageMath parsed files[m[41m[m
[32m+[m[32m*.sage.py[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Environments[m[41m[m
[32m+[m[32m.env[m[41m[m
[32m+[m[32m.venv[m[41m[m
[32m+[m[32menv/[m[41m[m
[32m+[m[32mvenv/[m[41m[m
[32m+[m[32mENV/[m[41m[m
[32m+[m[32menv.bak/[m[41m[m
[32m+[m[32mvenv.bak/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Spyder project settings[m[41m[m
[32m+[m[32m.spyderproject[m[41m[m
[32m+[m[32m.spyproject[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Rope project settings[m[41m[m
[32m+[m[32m.ropeproject[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# mkdocs documentation[m[41m[m
[32m+[m[32m/site[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# mypy[m[41m[m
[32m+[m[32m.mypy_cache/[m[41m[m
[32m+[m[32m.dmypy.json[m[41m[m
[32m+[m[32mdmypy.json[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Pyre type checker[m[41m[m
[32m+[m[32m.pyre/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# pytype static type analyzer[m[41m[m
[32m+[m[32m.pytype/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Cython debug symbols[m[41m[m
[32m+[m[32mcython_debug/[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# PyCharm[m[41m[m
[32m+[m[32m#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can[m[41m[m
[32m+[m[32m#  be found at https://github.com/git