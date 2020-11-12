# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

VM vs App Service comparison:
------------------------------------------------------------------------------------
             VM                                      App Service
    + cost more than app service                + cost less than VM
    + labor intensive                           + all handle by Azure
    + high availability and scaling             + hardware limitation to 14GB Max RAM & max of 4vCPUs
    + flexible types and sizes                  + highly available but with limitation in sizes
    + full control of the VM                    + don't have control of the VM at all
    + support multiple programming              + cost still continue to accumuate even if not used
        languages but are limited.              + auto scaling                               
                                                + support CD/CI flow
                                                + support multiple programming languages but are limited.


Why I picked App Service over VM for this project:
--------------------------------------------------

    I picked Web App as a service to deploy this project because it's lightweight and there are no requirements to have any restrictions to have a dedicated servers or number of CPU.  The App Service environment is within the boundary of the initial launch of the application.
    

Assess app changes that would change my decision:
-------------------------------------------------

If the number of users and the volume of articles being generated are increasing dramatically that the current App Service limitation is reached, a decicated VM may be needed for better performance.