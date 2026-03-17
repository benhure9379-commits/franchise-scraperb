import React, { useState } from 'react';
import { 
  BookOpen, 
  CheckCircle, 
  Clock, 
  Target, 
  ShieldCheck, 
  ArrowRight, 
  MessageSquare, 
  FileText, 
  TrendingUp, 
  User,
  Menu,
  X,
  ChevronRight,
  Download
} from 'lucide-react';

const App = () => {
  const [activePersona, setActivePersona] = useState(0);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [formSubmitted, setFormSubmitted] = useState(false);

  const personas = [
    {
      title: "20대 초중반",
      subtitle: "자본·경험 부족이 고민인 사회초년생",
      problem: "빨리 부를 만들고 싶지만 한 번의 실수가 무서워요.",
      solution: "초보를 위한 기초 가이드와 1:1 입문 브리핑",
      icon: <Target className="w-6 h-6" />
    },
    {
      title: "30-40대 직장인",
      subtitle: "월급 외 파이프라인이 절실한 분",
      problem: "공부할 시간은 없고, 믿을 만한 정보만 골라보고 싶어요.",
      solution: "후보 물건 자동 스크리닝 및 핵심 요약 리포트",
      icon: <TrendingUp className="w-6 h-6" />
    },
    {
      title: "50-60대",
      subtitle: "제2의 인생, 안전한 자산 관리가 목표인 분",
      problem: "절차가 너무 복잡하고 용어도 어려워서 막막합니다.",
      solution: "쉬운 언어로 풀이한 해석형 브리핑과 단계별 실행 지원",
      icon: <ShieldCheck className="w-6 h-6" />
    },
    {
      title: "시간 부족형",
      subtitle: "바쁜 일상 속 효율적 투자를 원하는 분",
      problem: "대신 분석해주고 리스크만 체크해줄 전문가가 필요해요.",
      solution: "입찰 전후 프로세스 대행 및 맞춤형 체크리스트",
      icon: <Clock className="w-6 h-6" />
    }
  ];

  const services = [
    {
      id: "briefing",
      title: "1건 해석형 브리핑",
      tag: "진입장벽 낮음",
      description: "특정 물건의 권리분석부터 가치 판단까지, 초보자도 이해하기 쉬운 언어로 정리해 드립니다.",
      price: "저가형 / 단건",
      features: ["위험요소 정밀 체크", "수익률 시뮬레이션", "핵심 포인트 요약"]
    },
    {
      id: "check",
      title: "입찰 전 체크 패키지",
      tag: "실행 직전 필수",
      description: "입찰장에 가기 전, 실수 없는 투자를 위해 서류와 절차를 최종 점검하는 패키지입니다.",
      price: "패키지형",
      features: ["현장 조사 가이드", "입찰 서류 완벽 검토", "낙찰 후 시나리오 제공"]
    },
    {
      id: "support",
      title: "낙찰 후 실행지원",
      tag: "핵심 프리미엄",
      description: "낙찰 이후 명도부터 사후 관리까지, 실제 수익을 확정 짓는 전 과정을 함께합니다.",
      price: "고단가 / 밀착지원",
      features: ["명도 로드맵 설계", "대출 및 세무 연결", "최종 수익 확정 가이드"]
    }
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    setFormSubmitted(true);
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans selection:bg-blue-100">
      {/* Navigation */}
      <nav className="fixed w-full bg-white/80 backdrop-blur-md z-50 border-b border-slate-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <ShieldCheck className="white text-white w-5 h-5" />
              </div>
              <span className="text-xl font-bold tracking-tight text-blue-900">경매마스터 브리핑</span>
            </div>
            
            <div className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600">
              <a href="#persona" className="hover:text-blue-600 transition-colors">맞춤 솔루션</a>
              <a href="#services" className="hover:text-blue-600 transition-colors">서비스 안내</a>
              <a href="#ebook" className="hover:text-blue-600 transition-colors">무료 전자책</a>
              <button 
                onClick={() => document.getElementById('consulting').scrollIntoView({behavior: 'smooth'})}
                className="bg-blue-600 text-white px-5 py-2 rounded-full hover:bg-blue-700 transition-all shadow-md shadow-blue-100"
              >
                상담 신청하기
              </button>
            </div>

            <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
              {isMenuOpen ? <X /> : <Menu />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden bg-white border-b border-slate-100 p-4 space-y-4 shadow-xl">
            <a href="#persona" className="block text-lg font-medium">맞춤 솔루션</a>
            <a href="#services" className="block text-lg font-medium">서비스 안내</a>
            <a href="#ebook" className="block text-lg font-medium">무료 전자책</a>
            <button className="w-full bg-blue-600 text-white py-3 rounded-xl font-bold">상담 신청하기</button>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4 bg-gradient-to-b from-blue-50 to-slate-50 overflow-hidden">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="space-y-8 animate-in fade-in slide-in-from-left duration-700">
              <div className="inline-flex items-center gap-2 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold uppercase tracking-wider">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                </span>
                정보가 아닌 실행을 팝니다
              </div>
              <h1 className="text-4xl md:text-6xl font-extrabold text-slate-900 leading-[1.15]">
                혼자 공부하는 경매는 끝내고, <br />
                <span className="text-blue-600">성공의 로드맵</span>을 사세요.
              </h1>
              <p className="text-lg text-slate-600 leading-relaxed max-w-lg">
                단순한 물건 리스트가 아닙니다. <br />
                당신의 불안을 확신으로 바꿔주는 정밀 브리핑과 실전 실행 지원을 통해 실수를 제로로 만듭니다.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button 
                  onClick={() => document.getElementById('consulting').scrollIntoView({behavior: 'smooth'})}
                  className="bg-blue-600 text-white px-8 py-4 rounded-2xl font-bold text-lg hover:bg-blue-700 transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-200"
                >
                  무료 상담 신청하기 <ChevronRight className="w-5 h-5" />
                </button>
                <button 
                  onClick={() => document.getElementById('ebook').scrollIntoView({behavior: 'smooth'})}
                  className="bg-white border-2 border-blue-100 text-blue-700 px-8 py-4 rounded-2xl font-bold text-lg hover:border-blue-600 transition-all flex items-center justify-center gap-2"
                >
                  무료 전자책 받기 <Download className="w-5 h-5" />
                </button>
              </div>
            </div>
            <div className="relative animate-in fade-in slide-in-from-right duration-700">
              <div className="bg-white p-8 rounded-[2rem] shadow-2xl border border-slate-100 relative z-10">
                <div className="flex items-center justify-between mb-6">
                  <span className="font-bold text-slate-400">Step 01. 분석 브리핑</span>
                  <div className="bg-green-100 text-green-700 text-xs font-bold px-2 py-1 rounded">안전 등급: A</div>
                </div>
                <div className="space-y-4">
                  <div className="h-4 w-3/4 bg-slate-100 rounded"></div>
                  <div className="h-4 w-1/2 bg-slate-100 rounded"></div>
                  <div className="pt-4 space-y-3">
                    <div className="flex items-center gap-3">
                      <CheckCircle className="text-blue-600 w-5 h-5" />
                      <span className="text-sm font-medium">대항력 없는 임차인으로 안전함</span>
                    </div>
                    <div className="flex items-center gap-3">
                      <CheckCircle className="text-blue-600 w-5 h-5" />
                      <span className="text-sm font-medium">관리비 미납금 23만원 확인 완료</span>
                    </div>
                    <div className="flex items-center gap-3 text-red-500">
                      <ShieldCheck className="w-5 h-5" />
                      <span className="text-sm font-medium">단, 점유자 이사 일자 협의 필요</span>
                    </div>
                  </div>
                  <div className="mt-6 p-4 bg-blue-50 rounded-xl">
                    <p className="text-xs text-blue-700 font-bold mb-1">전문가 의견</p>
                    <p className="text-sm text-blue-800 italic">"실거주 목적이라면 현재 최저가 대비 5% 상향 입찰을 추천합니다."</p>
                  </div>
                </div>
              </div>
              <div className="absolute -top-10 -right-10 w-64 h-64 bg-blue-200 rounded-full blur-3xl opacity-30 -z-10"></div>
              <div className="absolute -bottom-10 -left-10 w-64 h-64 bg-indigo-200 rounded-full blur-3xl opacity-30 -z-10"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Persona Section */}
      <section id="persona" className="py-24 px-4 bg-white">
        <div className="max-w-7xl mx-auto text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4">"내 얘긴가?" 싶다면 잘 오셨습니다.</h2>
          <p className="text-slate-500 max-w-2xl mx-auto">상황에 따라 필요한 도움은 모두 다릅니다. 당신의 현재 상태를 선택해보세요.</p>
        </div>

        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
            {personas.map((persona, index) => (
              <button
                key={index}
                onClick={() => setActivePersona(index)}
                className={`p-6 rounded-3xl transition-all text-left border-2 ${
                  activePersona === index 
                    ? 'border-blue-600 bg-blue-50 ring-4 ring-blue-50' 
                    : 'border-slate-100 hover:border-blue-200 bg-white'
                }`}
              >
                <div className={`w-12 h-12 rounded-2xl flex items-center justify-center mb-4 ${
                  activePersona === index ? 'bg-blue-600 text-white' : 'bg-slate-100 text-slate-400'
                }`}>
                  {persona.icon}
                </div>
                <h3 className="font-bold text-lg mb-1">{persona.title}</h3>
                <p className="text-xs text-slate-400 font-medium">{persona.subtitle}</p>
              </button>
            ))}
          </div>

          <div className="mt-10 p-8 md:p-12 bg-slate-900 rounded-[3rem] text-white relative overflow-hidden">
            <div className="relative z-10 md:flex items-center justify-between gap-12">
              <div className="space-y-4 md:w-2/3">
                <div className="inline-block px-3 py-1 bg-blue-600 rounded-full text-xs font-bold uppercase">상황별 맞춤 브리핑</div>
                <h4 className="text-2xl md:text-3xl font-bold leading-snug">
                  "{personas[activePersona].problem}"
                </h4>
                <div className="h-1 w-20 bg-blue-600 rounded-full"></div>
                <p className="text-slate-300 text-lg">
                  <span className="text-blue-400 font-bold">해결책: </span>
                  {personas[activePersona].solution}
                </p>
              </div>
              <div className="mt-8 md:mt-0 md:w-1/3">
                <button 
                  onClick={() => document.getElementById('services').scrollIntoView({behavior: 'smooth'})}
                  className="w-full bg-white text-slate-900 py-4 rounded-2xl font-bold hover:bg-blue-50 transition-colors flex items-center justify-center gap-2"
                >
                  해결책 자세히 보기 <ArrowRight className="w-5 h-5" />
                </button>
              </div>
            </div>
            <div className="absolute top-0 right-0 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl"></div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="py-24 px-4 bg-slate-50">
        <div className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
            <div className="space-y-4">
              <h2 className="text-3xl md:text-4xl font-extrabold text-slate-900">제대로 된 도움 하나가 <br />수천만 원의 가치를 만듭니다.</h2>
              <p className="text-slate-500">당신의 단계에 맞는 서비스를 선택하세요.</p>
            </div>
            <div className="bg-white p-2 rounded-2xl border border-slate-200 flex gap-2">
              <div className="px-4 py-2 bg-blue-600 text-white rounded-xl text-sm font-bold shadow-md shadow-blue-100">전문 브리핑</div>
              <div className="px-4 py-2 text-slate-400 text-sm font-bold">실행 지원</div>
            </div>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {services.map((service) => (
              <div key={service.id} className="bg-white p-8 rounded-[2.5rem] border border-slate-100 hover:shadow-2xl hover:-translate-y-2 transition-all group">
                <div className="mb-6">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-blue-600 bg-blue-50 px-2 py-1 rounded">
                    {service.tag}
                  </span>
                </div>
                <h3 className="text-2xl font-extrabold mb-4 group-hover:text-blue-600 transition-colors">{service.title}</h3>
                <p className="text-slate-500 text-sm leading-relaxed mb-8">
                  {service.description}
                </p>
                
                <ul className="space-y-4 mb-10">
                  {service.features.map((feature, i) => (
                    <li key={i} className="flex items-center gap-3 text-sm font-medium text-slate-700">
                      <div className="w-5 h-5 bg-blue-50 rounded-full flex items-center justify-center">
                        <CheckCircle className="w-3.5 h-3.5 text-blue-600" />
                      </div>
                      {feature}
                    </li>
                  ))}
                </ul>
                
                <div className="pt-6 border-t border-slate-50">
                  <div className="flex items-center justify-between mb-6">
                    <span className="text-slate-400 text-xs font-bold uppercase">가격 모델</span>
                    <span className="font-extrabold text-slate-900">{service.price}</span>
                  </div>
                  <button className="w-full py-4 bg-slate-900 text-white rounded-2xl font-bold hover:bg-blue-600 transition-colors shadow-lg shadow-slate-200">
                    상세 구성 확인하기
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* E-book Section (Lead Magnet) */}
      <section id="ebook" className="py-24 px-4 bg-white relative overflow-hidden">
        <div className="max-w-7xl mx-auto">
          <div className="bg-blue-600 rounded-[3rem] p-10 md:p-20 text-white flex flex-col md:flex-row items-center gap-12 relative overflow-hidden shadow-2xl shadow-blue-200">
            <div className="md:w-1/2 space-y-6 relative z-10">
              <div className="inline-flex items-center gap-2 px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-xs font-bold">
                <BookOpen className="w-4 h-4" /> 무료 증정 이벤트
              </div>
              <h2 className="text-3xl md:text-5xl font-extrabold leading-tight">
                경매 고수들은 절대 <br />알려주지 않는 <br />
                <span className="text-blue-200">'리스크 선별 필터링'</span>
              </h2>
              <p className="text-blue-100 text-lg font-medium">
                이미 1,200명이 다운로드 받았습니다. <br />
                이름과 연락처만 남기고 5분 만에 전문가의 시각을 얻으세요.
              </p>
              <ul className="space-y-3 pt-4">
                <li className="flex items-center gap-3">
                  <div className="w-6 h-6 bg-white/10 rounded-full flex items-center justify-center">
                    <CheckCircle className="w-4 h-4" />
                  </div>
                  <span>입찰 전 3분 만에 끝내는 권리분석 체크리스트</span>
                </li>
                <li className="flex items-center gap-3">
                  <div className="w-6 h-6 bg-white/10 rounded-full flex items-center justify-center">
                    <CheckCircle className="w-4 h-4" />
                  </div>
                  <span>초보자가 가장 많이 당하는 사기 유형 5가지</span>
                </li>
              </ul>
              <div className="pt-4 flex flex-col sm:flex-row gap-4">
                <input 
                  type="email" 
                  placeholder="이메일 주소를 입력하세요" 
                  className="px-6 py-4 rounded-2xl bg-white text-slate-900 w-full sm:w-auto focus:outline-none focus:ring-4 focus:ring-blue-300"
                />
                <button className="bg-slate-900 text-white px-8 py-4 rounded-2xl font-bold hover:bg-slate-800 transition-colors whitespace-nowrap">
                  무료로 받기
                </button>
              </div>
              <p className="text-xs text-blue-200 opacity-70">개인정보는 전자책 발송 용도로만 사용됩니다.</p>
            </div>
            
            <div className="md:w-1/2 flex justify-center relative">
              <div className="relative w-64 h-80 bg-white rounded-xl shadow-2xl p-6 transform rotate-3 hover:rotate-0 transition-transform duration-500">
                <div className="absolute top-0 right-0 w-8 h-full bg-slate-100 rounded-r-xl shadow-inner"></div>
                <div className="h-full border-2 border-slate-100 rounded-lg p-4 flex flex-col justify-between">
                  <div>
                    <div className="w-10 h-2 bg-blue-600 mb-4"></div>
                    <h4 className="text-slate-900 font-extrabold text-xl mb-2">선별과 해석</h4>
                    <p className="text-slate-400 text-[10px]">불안을 확신으로 바꾸는 <br />경매 가이드북</p>
                  </div>
                  <div className="text-slate-400 text-[10px] font-bold border-t pt-2">
                    경매마스터 브리핑 팀 저
                  </div>
                </div>
              </div>
              <div className="absolute -z-10 w-80 h-80 bg-blue-400/20 rounded-full blur-3xl"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Consulting Section (Lead Collection) */}
      <section id="consulting" className="py-24 px-4 bg-slate-50">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-[3rem] border border-slate-100 shadow-xl overflow-hidden">
            <div className="bg-slate-900 p-8 md:p-12 text-white text-center">
              <h2 className="text-3xl font-extrabold mb-4">전문가에게 직접 상담하기</h2>
              <p className="text-slate-400">현재 처한 상황을 알려주시면 가장 최적화된 실행 로드맵을 제안해 드립니다.</p>
            </div>
            
            <div className="p-8 md:p-12">
              {!formSubmitted ? (
                <form className="space-y-8" onSubmit={handleSubmit}>
                  <div className="grid md:grid-cols-2 gap-6">
                    <div className="space-y-2">
                      <label className="text-sm font-bold text-slate-700">성함</label>
                      <input 
                        required
                        type="text" 
                        placeholder="이름을 입력하세요" 
                        className="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:border-blue-600 transition-colors"
                      />
                    </div>
                    <div className="space-y-2">
                      <label className="text-sm font-bold text-slate-700">연락처</label>
                      <input 
                        required
                        type="tel" 
                        placeholder="010-0000-0000" 
                        className="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:border-blue-600 transition-colors"
                      />
                    </div>
                  </div>

                  <div className="space-y-2">
                    <label className="text-sm font-bold text-slate-700">경매 경험</label>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                      {["처음이에요", "공부만 했어요", "입찰 경험 있음", "낙찰 경험 있음"].map((item) => (
                        <label key={item} className="relative group cursor-pointer">
                          <input type="radio" name="experience" className="peer sr-only" />
                          <div className="px-4 py-3 text-sm text-center bg-white border border-slate-200 rounded-xl peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-checked:text-blue-600 transition-all font-medium">
                            {item}
                          </div>
                        </label>
                      ))}
                    </div>
                  </div>

                  <div className="space-y-2">
                    <label className="text-sm font-bold text-slate-700">주요 고민 (막히는 부분)</label>
                    <textarea 
                      placeholder="예: 권리분석이 너무 어려워요 / 입찰가가 고민이에요 / 명도가 걱정됩니다 등" 
                      rows="4" 
                      className="w-full px-5 py-4 bg-slate-50 border border-slate-200 rounded-2xl focus:outline-none focus:border-blue-600 transition-colors resize-none"
                    ></textarea>
                  </div>

                  <div className="space-y-4">
                    <div className="flex items-start gap-3">
                      <input type="checkbox" required className="mt-1 w-4 h-4 text-blue-600 rounded" />
                      <p className="text-xs text-slate-500 leading-relaxed">
                        개인정보 수집 및 이용에 동의합니다. 상담을 위해 입력하신 정보는 안전하게 관리되며 상담 목적 외에는 사용되지 않습니다.
                      </p>
                    </div>
                    <button 
                      type="submit"
                      className="w-full bg-blue-600 text-white py-5 rounded-[1.5rem] font-extrabold text-lg hover:bg-blue-700 transition-all shadow-xl shadow-blue-100 flex items-center justify-center gap-2"
                    >
                      상담 신청하고 가이드 받기 <ArrowRight className="w-5 h-5" />
                    </button>
                  </div>
                </form>
              ) : (
                <div className="py-12 text-center space-y-6">
                  <div className="w-20 h-20 bg-green-100 text-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <CheckCircle className="w-10 h-10" />
                  </div>
                  <h3 className="text-2xl font-bold text-slate-900">신청이 완료되었습니다!</h3>
                  <p className="text-slate-600">
                    담당 전문가가 확인 후 24시간 이내에 (영업일 기준) <br /> 
                    기재하신 연락처로 직접 연락드리겠습니다.
                  </p>
                  <button 
                    onClick={() => setFormSubmitted(false)}
                    className="text-blue-600 font-bold hover:underline"
                  >
                    다시 작성하기
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-20 px-4 border-t border-slate-800">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-12 mb-16">
            <div className="space-y-6 col-span-1 md:col-span-2">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                  <ShieldCheck className="text-white w-5 h-5" />
                </div>
                <span className="text-xl font-bold tracking-tight">경매마스터 브리핑</span>
              </div>
              <p className="text-slate-400 max-w-sm leading-relaxed">
                우리는 단순한 정보를 팔지 않습니다. <br />
                당신의 소중한 자산을 지키고 키울 수 있는 <br />
                정확한 '판단'과 '실행'을 지원합니다.
              </p>
              <div className="flex gap-4">
                <div className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-blue-600 transition-colors cursor-pointer text-slate-400 hover:text-white">
                  <MessageSquare className="w-5 h-5" />
                </div>
                <div className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-blue-600 transition-colors cursor-pointer text-slate-400 hover:text-white">
                  <FileText className="w-5 h-5" />
                </div>
              </div>
            </div>
            
            <div className="space-y-6">
              <h4 className="font-bold text-lg">서비스</h4>
              <ul className="space-y-4 text-slate-400 text-sm font-medium">
                <li className="hover:text-white transition-colors cursor-pointer">1건 해석 브리핑</li>
                <li className="hover:text-white transition-colors cursor-pointer">입찰 전 체크 패키지</li>
                <li className="hover:text-white transition-colors cursor-pointer">낙찰 후 실행지원</li>
                <li className="hover:text-white transition-colors cursor-pointer">정기 구독 브리핑</li>
              </ul>
            </div>

            <div className="space-y-6">
              <h4 className="font-bold text-lg">고객 지원</h4>
              <ul className="space-y-4 text-slate-400 text-sm font-medium">
                <li className="hover:text-white transition-colors cursor-pointer">무료 전자책</li>
                <li className="hover:text-white transition-colors cursor-pointer">이용 약관</li>
                <li className="hover:text-white transition-colors cursor-pointer">개인정보 처리방침</li>
                <li className="hover:text-white transition-colors cursor-pointer">자주 묻는 질문(FAQ)</li>
              </ul>
            </div>
          </div>
          
          <div className="pt-8 border-t border-slate-800 flex flex-col md:flex-row justify-between items-center gap-6 text-slate-500 text-xs font-medium">
            <p>© 2024 Auction Master Briefing. All rights reserved.</p>
            <div className="flex gap-8">
              <span>상호명: (주)경매마스터브리핑</span>
              <span>사업자등록번호: 000-00-00000</span>
              <span>대표: 홍길동</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default App;