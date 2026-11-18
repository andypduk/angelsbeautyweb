// Editable Figma construction source. Run through Figma's use_figma tool.
const BOOKSY = 'https://angels9.booksy.com/a/';
const INSTAGRAM = 'https://www.instagram.com/angels.surrey/';
const officialLogoHash = '798fd9905f8e15c56ae8b748d5a592560ce5f619';
const facialPhotoHash = '0460f478c39f5765d79728e29e8c4563cc6cac4a';
const salonInteriorHash = '6c314c2666514896eaae18be6e699daf2d9e61b1';
const hashes = ['5948752b66b805e4cd54075505a92e1270171f30','59fc3a36cc215e1923b28ba7e5925713d68966c8','3522e6301718510cd6f96d899ef88e99f2a5a669','59810e5b28f6b0761a6961cb35ae340a27527646','8bf806fa131ed6f6d998cb1c33751873a9257ee7','79736813a9ca4edcccc63f2c0b3df1740553246e'];
const posts = ['De9M1ogNXQu','De9Mv5Vt4PZ','DfmbrOSDVE7','De9MhopNGll','De9McDVNCyf','De9MUv7tsN-'];
const prim = $fig.varCollection({name:'Angels / Primitives',modes:['Value']});
const sem = $fig.varCollection({name:'Angels / Semantic',modes:['Default']});
const colors = {paper:'#F7F4EF',ink:'#302A28',muted:'#6D615E',plum:'#382731',sand:'#EBE4DC',line:'#D9CEC5',white:'#FFFFFF'};
const c = {};
for (const [name,value] of Object.entries(colors)) {
  const p = prim.colorVar({name:'color/'+name,values:{Value:value},scopes:[]});
  c[name]=sem.colorVar({name:'color/'+name,values:{Default:p},scopes:['FRAME_FILL','SHAPE_FILL','TEXT_FILL','STROKE_COLOR']});
}
const space={};
for(const n of [8,12,16,24,32,48,64,80]) space[n]=sem.numVar({name:'space/'+n,values:{Default:n},scopes:['GAP']});
const fill = name => [{type:'SOLID',color:c[name]}];
const text=(characters,size=16,width,opts={})=>$fig.text({name:characters.slice(0,48),characters,fontName:{family:'DM Sans',style:'Regular'},fontSize:size,lineHeight:{unit:'PERCENT',value:150},fills:fill('ink'),...(width?{width,textAutoResize:'HEIGHT'}:{}),...opts});
const serif=(s,size,w,opts={})=>text(s,size,w,{fontName:{family:'Cormorant Garamond',style:'Regular'},lineHeight:{unit:'PERCENT',value:100},...opts});
const eyebrow=(s,w)=>text(s,11,w,{letterSpacing:{unit:'PIXELS',value:2},fontName:{family:'DM Sans',style:'Medium'}});
const stack=(name,width,children,opts={})=>$fig.autoLayout({name,layoutMode:'VERTICAL',width,layoutSizingHorizontal:'FIXED',itemSpacing:space[24],fills:[],...opts},children);
const row=(name,width,children,opts={})=>$fig.autoLayout({name,layoutMode:'HORIZONTAL',width,layoutSizingHorizontal:'FIXED',itemSpacing:space[24],counterAxisAlignItems:'CENTER',fills:[],...opts},children);
const line=w=>$fig.rectangle({name:'Hairline',width:w,height:1,fills:fill('line')});
const image=(name,hash,w,h)=>$fig.rectangle({name,width:w,height:h,fills:[{type:'IMAGE',imageHash:hash,scaleMode:'FILL'}]});
const links=[]; const anchors=[];
const button=$fig.component({name:'Angels / Booking link',x:-700,y:0,layoutMode:'HORIZONTAL',layoutSizingHorizontal:'HUG',layoutSizingVertical:'HUG',paddingLeft:space[24],paddingRight:space[24],paddingTop:space[16],paddingBottom:space[16],fills:fill('plum'),itemSpacing:space[16],counterAxisAlignItems:'CENTER'},[text('Book on Booksy',14,undefined,{fills:fill('paper'),fontName:{family:'DM Sans',style:'Medium'}}).textProp('Label')]);
const nav=$fig.component({name:'Angels / Text link',x:-700,y:100,layoutMode:'HORIZONTAL',layoutSizingHorizontal:'HUG',layoutSizingVertical:'HUG',paddingTop:space[12],paddingBottom:space[12],fills:[]},[text('View treatments',14).textProp('Label')]);
const booking=(label='Book on Booksy',width)=>{const n=$fig.instance(button,{name:label,props:{Label:label},...(width?{width,layoutSizingHorizontal:'FIXED',primaryAxisAlignItems:'CENTER'}:{})});links.push([n,BOOKSY]);return n;};
const link=(label,url)=>{const n=$fig.instance(nav,{name:label,props:{Label:label}});if(url)links.push([n,url]);return n;};
const officialLogo=$fig.component({name:'Angels / Official supplied logo',x:-700,y:850,width:260,height:260*490/1500,layoutMode:'VERTICAL',layoutSizingHorizontal:'FIXED',layoutSizingVertical:'FIXED',fills:[]},[$fig.rectangle({name:'Original gold logo / cropped canvas',width:260,height:260*490/1500,layoutSizingHorizontal:'FILL',layoutSizingVertical:'FILL',blendMode:'MULTIPLY',fills:[{type:'IMAGE',imageHash:officialLogoHash,scaleMode:'CROP',imageTransform:[[1500/2048,0,275/2048],[0,490/2048,780/2048]]}]})]);
const brand=(small=false)=>{const w=small?180:260;return $fig.instance(officialLogo,{name:'Angels official logo',width:w,height:w*490/1500,layoutSizingHorizontal:'FIXED',layoutSizingVertical:'FIXED'});};
const service=$fig.component({name:'Angels / Treatment category',x:-700,y:200,layoutMode:'VERTICAL',width:400,layoutSizingHorizontal:'FIXED',layoutSizingVertical:'HUG',itemSpacing:space[16],fills:[]},[
  image('Treatment photo',hashes[1],400,360).set({layoutSizingHorizontal:'FILL'}),
  serif('Nails, beautifully considered.',34,400,{layoutSizingHorizontal:'FILL'}).textProp('Title'),
  text('BIAB, gel manicures and expressive nail art.',15,400,{fills:fill('muted'),layoutSizingHorizontal:'FILL'}).textProp('Description'),
  text('View treatments on Booksy',13,400,{textDecoration:'UNDERLINE',layoutSizingHorizontal:'FILL'}),
]);
const cardChanges=[];
function card(title,desc,hash,w,h){const n=$fig.instance(service,{name:title,width:w,layoutSizingHorizontal:'FIXED',props:{Title:title,Description:desc}});cardChanges.push({n,hash,w,h});links.push([n,BOOKSY]);return n;}
const desktop=stack('01 / Homepage — Desktop 1440',1440,[],{x:0,y:0,itemSpacing:0,fills:fill('paper'),clipsContent:true});
const mobile=stack('02 / Homepage — Mobile 390',390,[],{x:1600,y:0,itemSpacing:0,fills:fill('paper'),clipsContent:true});
const sections={};
for(const [root,m] of [[desktop,false],[mobile,true]]){
 const W=m?390:1440, p=m?24:96, inner=W-p*2;
 const section=(name,children,opts={})=>stack(name,W,children,{paddingLeft:p,paddingRight:p,paddingTop:m?56:88,paddingBottom:m?56:88,itemSpacing:space[32],...opts});
 const headerLinks=['Treatments','The Angels experience','Instagram','Visit'];
 const header= m?row('Header',W,[brand(true),link('Menu')],{paddingLeft:24,paddingRight:24,paddingTop:16,paddingBottom:16,primaryAxisAlignItems:'SPACE_BETWEEN'}):row('Header',W,[brand(),row('Navigation',630,headerLinks.map(label=>{const n=link(label,label==='Instagram'?INSTAGRAM:undefined);if(label!=='Instagram')anchors.push([n,root,label]);return n;}),{primaryAxisAlignItems:'SPACE_BETWEEN'}),booking()],{paddingLeft:p,paddingRight:p,paddingTop:24,paddingBottom:24,primaryAxisAlignItems:'SPACE_BETWEEN'});
 root.append(header);
 const heroCopy=stack('Hero copy',m?inner:560,[eyebrow('WEST CLANDON · SURREY',m?inner:560),serif('A little time.\nEntirely yours.',m?58:88,m?inner:560),text('Nails, lashes, brows and beauty treatments, with time and care dedicated to you.',m?16:18,m?inner:415,{fills:fill('muted')}),m?booking('Book on Booksy',inner):row('Hero actions',500,[booking(),link('View treatments')],{itemSpacing:32}),text('A private garden salon. A personal experience.',12,m?inner:480,{fills:fill('muted')})],{itemSpacing:space[24]});
 const heroPhoto=stack('Real Angels work',m?inner:560,[image('Angels nail art / Instagram De9Mv5Vt4PZ',hashes[1],m?inner:560,m?380:600),row('Image caption',m?inner:560,[text('THE ART IS IN THE DETAILS',10),text('@angels.surrey',11)],{primaryAxisAlignItems:'SPACE_BETWEEN'})],{itemSpacing:space[12]});
 root.append(section('Hero',m?[heroCopy,heroPhoto]:[row('Hero columns',inner,[heroCopy,heroPhoto],{itemSpacing:64,primaryAxisAlignItems:'SPACE_BETWEEN'})],{paddingTop:m?24:36,paddingBottom:m?48:64}));
 const promise=m?stack('Salon details',inner,[eyebrow('ONE-TO-ONE CARE'),eyebrow('BY APPOINTMENT'),eyebrow('WEST CLANDON, GUILDFORD')],{itemSpacing:space[16]}):row('Salon details',inner,[eyebrow('ONE-TO-ONE CARE'),eyebrow('BY APPOINTMENT'),eyebrow('WEST CLANDON, GUILDFORD')],{primaryAxisAlignItems:'SPACE_BETWEEN'});
 root.append(section('Details strip',[line(inner),promise,line(inner)],{paddingTop:0,paddingBottom:m?8:0,itemSpacing:space[24]}));
 const treatment=section('Treatments',[eyebrow('YOUR BEAUTY, YOUR WAY'),serif('Small details.\nA beautiful difference.',m?46:64,inner),text('Choose your treatment. Find current prices and appointments on Booksy.',16,m?inner:650,{fills:fill('muted')}),
  m?stack('Treatment categories',inner,[card('Nails & nail art','BIAB, gel manicures and nail art with personality.',hashes[1],inner,330),card('Lashes & brows','Lash lifts, brow lamination, shaping and tinting.',hashes[5],inner,330),card('Skin & aesthetics','Facials and aesthetic appointments tailored to you.',facialPhotoHash,inner,330)],{itemSpacing:space[48]}):row('Treatment categories',inner,[card('Nails & nail art','BIAB, gel manicures and nail art with personality.',hashes[1],400,360),card('Lashes & brows','Lash lifts, brow lamination, shaping and tinting.',hashes[5],400,360),card('Skin & aesthetics','Facials and aesthetic appointments tailored to you.',facialPhotoHash,400,360)],{counterAxisAlignItems:'MIN'}),
  text('Some treatments require a patch test or consultation. Check the service details before booking.',13,m?inner:800,{fills:fill('muted')})]);
 root.append(treatment);sections[(m?'m':'d')+'Treatments']=treatment;
 const experience=section('The Angels experience',[eyebrow('A MOMENT AWAY FROM THE EVERYDAY'),serif('Your appointment.\nYour space to unwind.',m?46:68,inner,{fills:fill('paper')}),text('Welcome to Angels, a private garden salon in West Clandon. Enjoy a relaxed, one-to-one appointment with Macy, with treatments chosen around you.',m?16:18,m?inner:620,{fills:fill('paper')}),line(inner),m?stack('Experience details',inner,[text('01  One-to-one appointments',16,inner,{fills:fill('paper')}),text('02  A private garden setting',16,inner,{fills:fill('paper')}),text('03  Time dedicated to you',16,inner,{fills:fill('paper')})]):row('Experience details',inner,['01  One-to-one appointments','02  A private garden setting','03  Time dedicated to you'].map(s=>text(s,16,undefined,{fills:fill('paper')})),{primaryAxisAlignItems:'SPACE_BETWEEN'})],{fills:fill('plum')});
 experience.children[0].set({fills:fill('paper')});
 if(m){
  experience.addAt(0,image('Angels salon interior — supplied photograph',salonInteriorHash,342,456));
 }else{
  const copyNodes=experience.children.slice(0,3);
  copyNodes[1].set({width:600,textAutoResize:'HEIGHT'});
  copyNodes[2].set({width:600,textAutoResize:'HEIGHT'});
  experience.addAt(0,row('Salon experience columns',inner,[stack('Salon experience copy',600,copyNodes,{itemSpacing:space[32]}),image('Angels salon interior — supplied photograph',salonInteriorHash,584,650)],{itemSpacing:space[64]}));
 }
 root.append(experience);sections[(m?'m':'d')+'The Angels experience']=experience;
 const galleryPhotos=[1,5,4,0].map((idx,i)=>{const n=image('Instagram / '+posts[idx],hashes[idx],m?165:294,m?220:380);links.push([n,INSTAGRAM+'p/'+posts[idx]+'/']);return n;});
 root.append(section('Instagram',[eyebrow('FROM THE ANGELS CHAIR'),serif('The latest little details.',m?46:64,inner),text('A selection of nails, lashes and brows from @angels.surrey.',16,inner,{fills:fill('muted')}),m?stack('Instagram grid',inner,[row('Gallery row 1',inner,galleryPhotos.slice(0,2),{itemSpacing:12}),row('Gallery row 2',inner,galleryPhotos.slice(2),{itemSpacing:12})],{itemSpacing:space[12]}):row('Instagram gallery',inner,galleryPhotos,{itemSpacing:24}),link('See more on Instagram',INSTAGRAM)]));
 const faqData=[['How do I book?','Choose your service, check the latest price and select an available appointment on Booksy.'],['Do I need a patch test?','Lash and brow services may require a patch test at least 48 hours before your appointment. Check your chosen service on Booksy.'],['Where is the salon?','Angels is a private garden salon in West Clandon, Guildford, Surrey. Visits are by appointment.']];
 root.append(section('Before your visit',[eyebrow('A LITTLE GOOD TO KNOW'),serif('Make yourself at home.',m?46:64,inner),...faqData.map(([q,a])=>stack(q,inner,[line(inner),text(q,18,inner,{fontName:{family:'DM Sans',style:'Medium'}}),text(a,15,m?inner:780,{fills:fill('muted')})],{itemSpacing:space[16]}))],{fills:fill('sand')}));
 const visit=section('Visit',[eyebrow('WE SAVED A LITTLE SPACE FOR YOU'),serif('Your next moment\nstarts here.',m?52:80,inner),text('West Clandon, Guildford · Surrey',16,inner),booking('Book on Booksy',m?inner:undefined),text('Choose a treatment, see current prices and find your appointment on Booksy.',14,m?inner:570,{fills:fill('muted')})]);
 root.append(visit);sections[(m?'m':'d')+'Visit']=visit;
 root.append(section('Footer',[line(inner),m?stack('Footer identity',inner,[brand(),text('Beauty, with a personal touch.',14,inner),link('@angels.surrey',INSTAGRAM),link('Bookings & policies',BOOKSY)]):row('Footer identity',inner,[brand(),text('Beauty, with a personal touch.',14),link('@angels.surrey',INSTAGRAM),link('Bookings & policies',BOOKSY)],{primaryAxisAlignItems:'SPACE_BETWEEN'}),text('© 2026 Angels Clinic & Beauty',11,inner,{fills:fill('muted')})],{paddingTop:0,paddingBottom:32}));
}
const menu=stack('03 / Mobile menu — open',390,[row('Menu header',342,[brand(true),link('Close')],{primaryAxisAlignItems:'SPACE_BETWEEN'}),...['Treatments','The Angels experience','Instagram','Visit'].map(label=>{const n=link(label,label==='Instagram'?INSTAGRAM:undefined);if(label!=='Instagram')anchors.push([n,mobile,label]);return n;}),booking('Book on Booksy',342)],{x:2100,y:0,paddingTop:24,paddingBottom:32,paddingLeft:24,paddingRight:24,itemSpacing:space[24],fills:fill('paper')});
const notes=stack('04 / Design and integration notes',720,[eyebrow('ANGELS / DESIGN HANDOFF'),serif('Quiet luxury.\nPersonal care.',64,620),text('Desktop 1440 and mobile 390. Native editable text, auto-layout, shared colour and spacing variables, reusable booking, navigation and treatment components.',16,620),text('BOOKSY\nAll booking actions open the official profile link: '+BOOKSY+'\nPrices, availability and confirmation stay with Booksy. No booking is made by this prototype.',16,620),text('INSTAGRAM\nSix real photographs captured from the public @angels.surrey profile on 18 November 2026. Gallery tiles link to their source posts. This is a curated design snapshot, not an automatically updating feed. Confirm client image permissions before publishing.',16,620),text('LIVE FEED HANDOFF\nConnect an authorised Instagram professional account through a supported Meta integration or approved feed provider. Refresh and cache on the server; keep tokens private. If refresh fails, retain the last authorised gallery and a working Instagram link. Include empty, loading and disconnected states. No Meta connection or tracking is activated.',16,620),text('RESPONSIVE / ACCESSIBILITY\nReflow to one column, 24px mobile gutters and a 2-column gallery. Navigation uses a menu on mobile. Booking links have 48px+ targets. Browser keyboard, zoom, screen-reader and performance testing follow during implementation.',16,620),text('CONTENT\nBusiness and treatment categories checked against Booksy and the public Instagram profile. No invented testimonials, results, credentials or discounts. Official gold logo supplied by Andy, used in headers, footers and mobile menu. Original JPEG preserved; whitespace cropped in Figma with Multiply blending on light surfaces. Raster artwork, not a vector or transparent asset.',16,620)],{x:2600,y:0,paddingTop:48,paddingBottom:48,paddingLeft:48,paddingRight:48,itemSpacing:space[32],fills:fill('sand')});
await $fig.done();
for(const {n,hash,w,h} of cardChanges){
 $fig.query('RECTANGLE[name="Treatment photo"]',n.node).set({width:w,height:h,fills:[hash===facialPhotoHash?{type:'IMAGE',imageHash:hash,scaleMode:'CROP',imageTransform:[[1,0,0],[0,h/w/(2399/1600),0]]}:{type:'IMAGE',imageHash:hash,scaleMode:'FILL'}]});
 $fig.query('TEXT',n.node).set({width:w,textAutoResize:'HEIGHT'});
}
await $fig.done();
for(const [node,url] of links) await node.node.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'URL',url,openInNewTab:true}]}]);
for(const [node,root,label] of anchors){const target=sections[(root===mobile?'m':'d')+label];if(target)await node.node.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:target.node.id,navigation:'SCROLL_TO',transition:null}]}]);}
const menus=mobile.node.query('INSTANCE[name="Menu"]').toArray();
for(const n of menus) await n.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:menu.node.id,navigation:'NAVIGATE',transition:null}]}]);
const close=menu.node.query('INSTANCE[name="Close"]').first();
if(close) await close.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:mobile.node.id,navigation:'NAVIGATE',transition:null}]}]);
const heroTreatment=desktop.node.query('INSTANCE[name="View treatments"]').first();
if(heroTreatment)await heroTreatment.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:sections.dTreatments.node.id,navigation:'SCROLL_TO',transition:null}]}]);
// Keep imported source assets away from the customer-facing compositions.
['1:321','1:322','1:323','1:324','1:325','1:326'].forEach((id,i)=>$fig.get(id).set({x:-1500,y:1200+i*700,name:'Instagram source asset '+i}));
await $fig.done();
return {desktop:{id:desktop.node.id,width:desktop.node.width,height:desktop.node.height},mobile:{id:mobile.node.id,width:mobile.node.width,height:mobile.node.height},menu:menu.node.id,notes:notes.node.id,linkedActions:links.length,fonts:[...new Set(desktop.node.query('TEXT').toArray().map(n=>n.fontName.family))]};
