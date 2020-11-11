# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

VM Analysis:
    + cost more than app service
    + labor intensive
    + high availability and scaling
    + flexible types and sizes
    + full control of the VM



App Service analysis:
    + cost less than VM
    + auto scaling
    + support CD
    + support multi prg languages but are limited
    + hardware limitation to 14GB Max RAM
    + max of 4vCPUs
    + cost still occurring even if not used

I picked Web App as a service to deploy this project because it's lightweight and there are no requirements to have restrictions on dedicated servers.  It's within the boundary of the initial launch of the application.  If more and more users need to be accomodated than a decicated VM may be needed for performance.

URL link to the web app:  http://articlecmstoazurewebapp.azurewebsites.net/