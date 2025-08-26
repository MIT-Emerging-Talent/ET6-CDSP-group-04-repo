(function(){
  const PLAN_MAP = {
    '2-4y:none': {title:'Community College pathway (low-cost)',desc:'Associate degree/transfer with aid + stack a cert.',steps2w:['Advisor meeting; map transfer options.','Complete FAFSA/aid & fee waivers.','Choose a cert (AWS CC) + schedule.'],steps3m:['Enroll 2–3 core IT courses.','Start GitHub + LinkedIn.','Attend 1–2 employer events.']},
    '2-4y:some': {title:'Degree/CC transfer + early internships',desc:'Progress degree + early internships; funds for books/fees/certs.',steps2w:['Degree map + internship advising.','Join career portal; draft 1-page resume.','Book a cert date.'],steps3m:['Apply to 5 campus IT roles.','Finish 2–3 portfolio artifacts.','Attend 2 meetups/hackathons.']},
    '2-4y:more': {title:'University + co-op',desc:'Recognized CS/IT degree with co-op; targeted certs.',steps2w:['Shortlist co-op programs; compare outcomes.','Contact admissions + aid.','Plan cert track (AZ-900).'],steps3m:['Secure co-op timeline; network.','Ship 2–3 public projects.','Weekly interview practice.']},
    '6-12m:none': {title:'Apprenticeships / WIOA-funded training',desc:'Short subsidized training with placement support.',steps2w:['American Job Center → ask WIOA.','Find 2 nonprofits; join waitlists.','Start a free study plan + repo.'],steps3m:['Finish coursework; resume review.','Apply to 10 apprentice/helpdesk roles.','Add a tiny capstone/portfolio site.']},
    '6-12m:some': {title:'Low-cost bootcamp + cert',desc:'Affordable bootcamp/CC cert + entry cert + part-time work.',steps2w:['Compare 3 programs by outcomes.','Block weekly schedule + office hours.','Book cert date.'],steps3m:['Build 2–3 real projects.','3 informational interviews.','Apply to 15 roles; iterate resume.']},
    '6-12m:more': {title:'Reputable bootcamp + employer network',desc:'Outcomes-backed bootcamp with pipelines.',steps2w:['Verify audited outcomes; talk to alumni.','Baseline assessment + pre-work.','Draft LinkedIn + site.'],steps3m:['Complete capstone.','2 mock interviews/week.','Use partner referrals broadly.']},
    '<3m:none': {title:'Free online learning + public resources',desc:'Start now with free courses; build tiny real projects.',steps2w:['Pick one path and one course.','Create GitHub; push daily notes.','Book resume review at job center.'],steps3m:['Ship 3 tiny projects + READMEs.','Take entry cert if feasible.','Apply to 10–20 entry roles.']},
    '<3m:some': {title:'Short certificate + portfolio sprint',desc:'Invest small funds in a short cert and demos.',steps2w:['Enroll in AZ-900/Google IT.','Choose 2 portfolio ideas.','Set weekly demo day.'],steps3m:['Finish cert; add badge.','Record 60–90s project videos.','Apply to 15 roles; seek referrals.']},
    '<3m:more': {title:'Intro bootcamp + coaching',desc:'Intensive foundations + coaching + interview prep.',steps2w:['Skills assessment + pre-work.','Weekly mock interviews.','List mentors/alumni.'],steps3m:['1–2 showcase projects aligned to postings.','Iterate resume/LinkedIn weekly.','Apply to 15–25 roles; target apprenticeships.']}
  };

  function h(tag, attrs={}, children=[]) {
    const el = document.createElement(tag);
    for (const [k,v] of Object.entries(attrs||{})) {
      if (k === 'class') el.className = v;
      else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
      else if (k === 'html') el.innerHTML = v;
      else el.setAttribute(k, v);
    }
    (Array.isArray(children)?children:[children]).filter(Boolean).forEach(c => {
      if (typeof c === 'string') el.appendChild(document.createTextNode(c)); else el.appendChild(c);
    });
    return el;
  }

  function mountPlanner(selector){
    const root = document.querySelector(selector);
    if(!root) return;
    const state = { time:null, money:null };

    // Elements
    const timeChoices = h('div', {class:'choices', id:'time-choices'}, [
      h('button', {class:'btn', type:'button', 'data-time':'2-4y'}, '2–4 years'),
      h('button', {class:'btn', type:'button', 'data-time':'6-12m'}, '6–12 months'),
      h('button', {class:'btn', type:'button', 'data-time':'<3m'}, '< 3 months')
    ]);

    const moneyChoices = h('div', {class:'choices', id:'money-choices'}, [
      h('button', {class:'btn', type:'button', 'data-money':'none'}, 'None'),
      h('button', {class:'btn', type:'button', 'data-money':'some'}, 'Some ($500–$3k)'),
      h('button', {class:'btn', type:'button', 'data-money':'more'}, 'More ($3k+ or aid)')
    ]);

    const grid = h('div', {class:'planner-grid'}, [
      h('div', {}, [h('div',{class:'label'},'1) Time you can invest now'), timeChoices]),
      h('div', {}, [h('div',{class:'label'},'2) Budget you can allocate'), moneyChoices])
    ]);

    const result = h('div', {class:'result', id:'result'}, [
      h('h2', {id:'path-title', style:'font-size:22px;font-weight:900'}, ''),
      h('p', {id:'path-desc', style:'color:#cfe1ff'}, ''),
      h('div', {class:'tiles'}, [
        h('strong', {}, 'Next 2 weeks'),
        h('ul', {class:'steps', id:'steps-2w'}),
        h('strong', {}, 'Next 2–3 months'),
        h('ul', {class:'steps', id:'steps-3m'})
      ])
    ]);

    const cta = h('button', {class:'primary', id:'see-plan', type:'button', disabled:true}, 'See my plan');
    const ctaWrap = h('div', {style:'display:flex;justify-content:center;margin-top:10px;'}, [cta]);

    root.appendChild(grid);
    root.appendChild(result);
    root.appendChild(ctaWrap);

    const $ = (sel)=>root.querySelector(sel);
    const $$ = (sel)=>Array.from(root.querySelectorAll(sel));

    function select(group, value){
      $$(group+' .btn').forEach(b=>{
        const isActive = (b.dataset.time === value) || (b.dataset.money === value);
        b.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });
    }

    function renderPlan(){
      const key = state.time + ':' + state.money;
      const plan = PLAN_MAP[key]; if(!plan) return;
      $('#path-title').textContent = plan.title;
      $('#path-desc').textContent  = plan.desc;
      const s2w = $('#steps-2w'); const s3m = $('#steps-3m');
      s2w.innerHTML=''; s3m.innerHTML='';
      (plan.steps2w||[]).forEach(t=>{ const li=document.createElement('li'); li.textContent=t; s2w.appendChild(li); });
      (plan.steps3m||[]).forEach(t=>{ const li=document.createElement('li'); li.textContent=t; s3m.appendChild(li); });
      $('#result').style.display='flex';
    }

    function updateCTA(){
      const btn = $('#see-plan');
      btn.disabled = !(state.time && state.money);
    }

    $('#time-choices').addEventListener('click', (e)=>{
      if(e.target.classList.contains('btn')){
        state.time = e.target.dataset.time; select('#time-choices', state.time); updateCTA();
      }
    });
    $('#money-choices').addEventListener('click', (e)=>{
      if(e.target.classList.contains('btn')){
        state.money = e.target.dataset.money; select('#money-choices', state.money); updateCTA();
      }
    });
    $('#see-plan').addEventListener('click', renderPlan);
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', ()=> mountPlanner('#planner-mount'));
  } else {
    mountPlanner('#planner-mount');
  }
})();