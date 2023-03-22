<div>
    Below is a list of all students who have signed up for this feature. We've 
    also included a preliminary scoring of their abilities using our new AI-based
    rating system.
</div>
<div class="career-block">
    {{{each allData}}}
        <div class="card" style="width: 28rem;">
            <div class="card-body">
                <div class="card-title">
                    {../student_id}
                </div>
                <div class="card-text">
                    Major: {../major} <br/>
                    GPA: {../gpa} <br/>
                    Extracurricular: {../extra_curricular} <br/>
                    # Prog Languages: {../num_programming_languages} <br/>
                    # Past Internships: {../num_past_internships} <br/>
                </div>
                <div class="prediction" style={function.getPredictionColor, ../prediction}>
                    {function.formatPrediction, ../prediction}
                </div>
            </div>
        </div>
    {{{end}}}    
</div>
