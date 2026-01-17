
var documents = [{
    "id": 0,
    "url": "http://localhost:4000/404.html",
    "title": "404",
    "body": "404 Page does not exist!Please use the search bar at the top or visit our homepage! "
    }, {
    "id": 1,
    "url": "http://localhost:4000/about",
    "title": "CV",
    "body": "I am Kyung-Min Jin, a master's student in the graduate school of Artificial Intelligence at Korea University (PRML Lab), where I am advised by Prof Seong-Hwan Lee. Before studying at graduate school, I received Bachelor's degrees (Computer Science and Engineering) and (Artificial Intelligence) at Korea University in 2021. Social Media and CVThank you! Visit my Github Profile Kyung-Min Jin . Linkedin Documentation CV"
    }, {
    "id": 2,
    "url": "http://localhost:4000/categories",
    "title": "Categories",
    "body": ""
    }, {
    "id": 3,
    "url": "http://localhost:4000/",
    "title": "Home",
    "body": "      Featured:                                                                                                       About Me                          1 2 3 4 5                       :                I am Kyung-Min Jin, a master’s student in the graduate school of Artificial Intelligence at Korea University (PRML Lab), where I am advised by Prof. . .        :                                                                                        Kyung-Min Jin                  13 May 2022                                                                             All Stories:             "
    }, {
    "id": 4,
    "url": "http://localhost:4000/robots.txt",
    "title": "",
    "body": "      Sitemap: {{ “sitemap. xml”   absolute_url }}   "
    }, {
    "id": 5,
    "url": "http://localhost:4000/about-me/",
    "title": "About Me",
    "body": "2022/05/13 - # Korean 저는 고려대학교 인공지능대학원 PRML 연구실에서 이성환 교수님의 지도 아래 석사 과정을 마친 진경민입니다. 대학원 진학 이전에는 고려대학교에서 컴퓨터공학과와 인공지능을 전공하여 2021년에 학사 학위를 취득했습니다. **시각 지각에서 시작해 체화된 추론으로 확장되는 멀티모달 지능을 연구합니다.** 저의 연구는 컴퓨터 비전 분야에서 시작되었으며, 트랜스포머 아키텍처와 합성곱 신경망을 결합한 새로운 포즈 추정 프레임워크를 제안해 다수의 벤치마크에서 최고 수준의 성능을 달성했습니다. 이러한 연구 성과를 바탕으로 WACV를 포함한 국제 학회 및 저널에 논문을 발표했습니다. 이후 LG전자에 합류하여 인체 및 손 포즈 추정 모델을 엣지 디바이스 환경에 적용하는 연구를 수행하며, 실제 환경에서의 효율성과 강건성을 중심으로 한 모델 개발에 참여했습니다. 연구 관심사는 점차 확장되어 Vision–Language–Audio 기반의 대규모 멀티모달 모델, cross-modal continual learning, 그리고 GRPO 및 DPO와 같은 강화학습 기반 정책 최적화 기법을 활용한 멀티모달 학습 연구를 진행했습니다.최근에는 로봇 선행 연구 조직에서 로봇 인지 및 자연어 기반 객체 이해 기술을 연구하고 있으며, 멀티모달 파운데이션 모델과 체화된 인공지능을 연결해 로봇이 시각 정보를 언어적으로 이해하고 물리적 환경과 효과적으로 상호작용할 수 있도록 하는 것을 목표로 하고 있습니다. # English I am Kyung-Min Jin, completed my master’s studies in the Graduate School of Artificial Intelligence at Korea University (PRML Lab), where I was advised by Prof Seong-Hwan Lee. Before studying at graduate school, I received Bachelor's degrees (Computer Science and Engineering) and (Artificial Intelligence) at Korea University in 2021.Seong-Hwan Lee. Building multimodal intelligence from visual perception to embodied reasoning. My research began in the computer vision domain, where I designed novel pose estimation frameworks that combine transformer-based architectures with convolutional neural networks. This work achieved state-of-the-art performance across multiple benchmarks and led to publications in international conferences and peer-reviewed journals, including WACV. After joining LG Electronics, I worked on deploying body and hand pose estimation models to edge devices, focusing on efficiency and robustness in real-world environments. As my research interests expanded, I transitioned toward multimodal learning, contributing to the development of large-scale Vision–Language–Audio models, cross-modal continual learning strategies, and reinforcement learning–based policy optimization methods such as GRPO and DPO. More recently, I have been working within an advanced robotics research team, where my focus is on robotic perception and natural language–based object understanding. My current research aims to bridge multimodal foundation models with embodied AI, enabling robots to ground language in visual perception and interact with the physical world more effectively. "
    }];

var idx = lunr(function () {
    this.ref('id')
    this.field('title')
    this.field('body')

    documents.forEach(function (doc) {
        this.add(doc)
    }, this)
});
function lunr_search(term) {
    document.getElementById('lunrsearchresults').innerHTML = '<ul></ul>';
    if(term) {
        document.getElementById('lunrsearchresults').innerHTML = "<p>Search results for '" + term + "'</p>" + document.getElementById('lunrsearchresults').innerHTML;
        //put results on the screen.
        var results = idx.search(term);
        if(results.length>0){
            //console.log(idx.search(term));
            //if results
            for (var i = 0; i < results.length; i++) {
                // more statements
                var ref = results[i]['ref'];
                var url = documents[ref]['url'];
                var title = documents[ref]['title'];
                var body = documents[ref]['body'].substring(0,160)+'...';
                document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML = document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML + "<li class='lunrsearchresult'><a href='" + url + "'><span class='title'>" + title + "</span><br /><span class='body'>"+ body +"</span><br /><span class='url'>"+ url +"</span></a></li>";
            }
        } else {
            document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML = "<li class='lunrsearchresult'>No results found...</li>";
        }
    }
    return false;
}

function lunr_search(term) {
    $('#lunrsearchresults').show( 400 );
    $( "body" ).addClass( "modal-open" );
    
    document.getElementById('lunrsearchresults').innerHTML = '<div id="resultsmodal" class="modal fade show d-block"  tabindex="-1" role="dialog" aria-labelledby="resultsmodal"> <div class="modal-dialog shadow-lg" role="document"> <div class="modal-content"> <div class="modal-header" id="modtit"> <button type="button" class="close" id="btnx" data-dismiss="modal" aria-label="Close"> &times; </button> </div> <div class="modal-body"> <ul class="mb-0"> </ul>    </div> <div class="modal-footer"><button id="btnx" type="button" class="btn btn-danger btn-sm" data-dismiss="modal">Close</button></div></div> </div></div>';
    if(term) {
        document.getElementById('modtit').innerHTML = "<h5 class='modal-title'>Search results for '" + term + "'</h5>" + document.getElementById('modtit').innerHTML;
        //put results on the screen.
        var results = idx.search(term);
        if(results.length>0){
            //console.log(idx.search(term));
            //if results
            for (var i = 0; i < results.length; i++) {
                // more statements
                var ref = results[i]['ref'];
                var url = documents[ref]['url'];
                var title = documents[ref]['title'];
                var body = documents[ref]['body'].substring(0,160)+'...';
                document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML = document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML + "<li class='lunrsearchresult'><a href='" + url + "'><span class='title'>" + title + "</span><br /><small><span class='body'>"+ body +"</span><br /><span class='url'>"+ url +"</span></small></a></li>";
            }
        } else {
            document.querySelectorAll('#lunrsearchresults ul')[0].innerHTML = "<li class='lunrsearchresult'>Sorry, no results found. Close & try a different search!</li>";
        }
    }
    return false;
}
    
$(function() {
    $("#lunrsearchresults").on('click', '#btnx', function () {
        $('#lunrsearchresults').hide( 5 );
        $( "body" ).removeClass( "modal-open" );
    });
});