<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="main bg-gray-50 text-gray-800 font-sans">
      <nav class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex justify-between items-center h-20">
            <div class="flex items-center gap-3">
              <img
                src="https://placehold.co/60x60/6366f1/white?text=K&font=raleway"
                alt="Karzo Logo"
                class="h-10 w-10 rounded-lg"
              />
              <span class="text-2xl font-bold text-gray-900">Karzo</span>
            </div>
  
            <div class="hidden md:flex items-center gap-8 text-base font-medium text-gray-600">
              <a href="#events" class="hover:text-indigo-600 transition duration-200 ease-in-out">Events</a>
              <a href="#feedback" class="hover:text-indigo-600 transition duration-200 ease-in-out">Testimonials</a>
              <a href="#blogs" class="hover:text-indigo-600 transition duration-200 ease-in-out">Blog</a>
            </div>
  
            <div class="flex items-center gap-3">
              <RouterLink :to="{ name: 'DRegisterView' }">
                <button class="px-4 py-2 text-sm font-semibold text-indigo-600 border border-indigo-200 rounded-md hover:bg-indigo-50 transition duration-200 ease-in-out">
                  Driver Portal
                </button>
              </RouterLink>
              <RouterLink :to="{ name: 'PRegisterView' }">
                <button class="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-700 transition duration-200 ease-in-out shadow-sm">
                  Passenger Sign Up
                </button>
              </RouterLink>
              </div>
          </div>
        </div>
      </nav>
  
      <section class="relative pt-16 pb-24 md:pt-24 md:pb-32 overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-indigo-50 via-white to-purple-50 opacity-60"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="text-center lg:text-left">
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-gray-900 leading-tight mb-6">
              Seamless Rides, <br class="hidden sm:inline" /> Unforgettable <span class="bg-gradient-to-br from-[#0C0C0C] via-[#0C0C0C] to-[#4834D4] text-transparent bg-clip-text">Events</span>.
            </h1>
            <p class="text-lg text-gray-600 mb-8 max-w-xl mx-auto lg:mx-0">
              Connect with drivers for instant rides or event transport. Join Karzo for reliable, fast, and safe journeys across the city.
            </p>
            <div class="flex flex-col sm:flex-row justify-center lg:justify-start gap-4 max-w-md mx-auto lg:mx-0">
              <input
                type="email"
                placeholder="Enter your email"
                class="flex-grow px-5 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-base"
              />
              <button class="px-6 py-3 bg-indigo-600 text-white font-semibold rounded-md shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-200 ease-in-out">
                Get Started
              </button>
            </div>
            <p class="text-sm text-gray-500 mt-4">Subscribe to our newsletter for updates.</p>
          </div>
  
          <div class="mt-10 lg:mt-0">
            <div class="bg-white rounded-xl shadow-2xl overflow-hidden aspect-video">
              <video
                src="https://videos.pexels.com/video-files/5834563/5834563-uhd_1440_2560_24fps.mp4"
                autoplay
                loop
                muted
                alt="Karzo Ride Booking"
                class="w-full h-full object-cover pointer-events-none"
              />
              </div>
          </div>
        </div>
      </section>
  
      <section class="py-16 md:py-24 bg-white" id="events">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
             <h2 class="text-base font-semibold text-indigo-600 tracking-wide uppercase">Explore</h2>
             <p class="mt-2 text-3xl lg:text-4xl font-extrabold text-gray-900 tracking-tight">Upcoming Local Events</p>
             <p class="mt-4 max-w-2xl text-lg text-gray-500 mx-auto">
               Find rides to the city's top happenings or share your journey.
             </p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
              <img src="https://imgs.search.brave.com/a4dDrisJOmUvKrqzhXSwAwRvPL2uqKk9k6sK2c5wbfg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/Y2FsZWlkb3Njb3Bl/LmluL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE2LzAyL2thbGEt/Z2hvZGEtYXJ0cy1m/ZXN0aXZhbC0zLmpw/Zw" alt="Kala Ghoda Fest" class="w-full h-48 object-cover">
              <div class="p-6">
                <p class="text-sm font-semibold text-indigo-600">Churchgate</p>
                <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200">Kala Ghoda Arts Festival</h3>
                <p class="text-sm text-gray-600 mb-4 line-clamp-2">Experience the vibrant celebration of arts and culture in the heart of Mumbai.</p>
                <div class="flex items-center text-xs text-gray-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1.5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                  <span>Feb 1st - Feb 9th, 2026</span>
                   <span class="ml-auto font-medium text-indigo-500 hover:text-indigo-700 cursor-pointer">Details & Rides &rarr;</span>
                </div>
              </div>
            </div>
  
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
              <img src="https://imgs.search.brave.com/lrnSGCOWLEwDhjyoU0qIdZbYnHZOiN84W3gz0QH5qV0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wcmV2/aWV3LnJlZGQuaXQv/c2hpdmFqaS1wYXJr/LWRhZGFyLWR1cmlu/Zy1kaXdhbGktdjAt/aTB4ZXdxZzdnZ3lk/MS5qcGc_d2lkdGg9/NjQwJmNyb3A9c21h/cnQmYXV0bz13ZWJw/JnM9ODgzZGFmOTNk/ZjU3M2VkZTE2NWM1/ZjkyMDliNjUyNGI5/ZWRkMGY0MA" alt="Shivaji Park Diwali" class="w-full h-48 object-cover">
              <div class="p-6">
                <p class="text-sm font-semibold text-indigo-600">Dadar</p>
                <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200">Shivaji Park Diwali Pahat</h3>
                <p class="text-sm text-gray-600 mb-4 line-clamp-2">Join the traditional early morning Diwali celebrations with music and community.</p>
                 <div class="flex items-center text-xs text-gray-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1.5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                  <span>Oct 25th, 2025 (Tentative)</span>
                   <span class="ml-auto font-medium text-indigo-500 hover:text-indigo-700 cursor-pointer">Details & Rides &rarr;</span>
                </div>
              </div>
            </div>
  
            <div class="bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
              <img src="https://imgs.search.brave.com/JYTLwugjKYb2FWcl26PGdzZ15e5m8gnuU6oVMbUSm_Y/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbS53/aGF0c2hvdC5pbi9p/bWcvMjAxOS9EZWMv/NDkwMTc3NzEtMjU5/MTM1MDkxNDIyMzQx/NS0yNjk3Njc5Mzc4/MjA4MjYwMDk2LW8t/MTU3NjIyODMxNC5q/cGc_d3A9MQ" alt="Mahim Fair" class="w-full h-48 object-cover">
              <div class="p-6">
                <p class="text-sm font-semibold text-indigo-600">Mahim</p>
                <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200">Mahim Fair (Mela)</h3>
                <p class="text-sm text-gray-600 mb-4 line-clamp-2">A vibrant local fair held annually, known for its unique stalls and festive atmosphere.</p>
                 <div class="flex items-center text-xs text-gray-500">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1.5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                  <span>Dec 15th - Dec 25th, 2025</span>
                   <span class="ml-auto font-medium text-indigo-500 hover:text-indigo-700 cursor-pointer">Details & Rides &rarr;</span>
                </div>
              </div>
            </div>
            </div>
          <div class="text-center mt-12">
              <button class="px-6 py-3 border border-indigo-600 text-indigo-600 font-semibold rounded-md hover:bg-indigo-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-200 ease-in-out">
                View All Events
              </button>
          </div>
        </div>
      </section>
  
      <section class="py-16 md:py-24 bg-gradient-to-b from-indigo-50 to-purple-50 overflow-hidden" id="feedback">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="text-center mb-12">
             <h2 class="text-base font-semibold text-indigo-600 tracking-wide uppercase">Testimonials</h2>
             <p class="mt-2 text-3xl lg:text-4xl font-extrabold text-gray-900 tracking-tight">Loved by Riders & Drivers</p>
             <p class="mt-4 max-w-2xl text-lg text-gray-500 mx-auto">
               Hear directly from our community about their Karzo experience.
             </p>
          </div>
  
          <div class="feedback-container relative overflow-hidden group">
             <div class="absolute top-0 bottom-0 left-0 w-16 bg-gradient-to-r from-indigo-50 to-transparent z-10"></div>
             <div class="absolute top-0 bottom-0 right-0 w-16 bg-gradient-to-l from-indigo-50 to-transparent z-10"></div>
  
             <div class="feedback-scroll flex gap-8 w-max animate-scroll group-hover:[animation-play-state:paused]">
               <template v-for="n in 2" :key="n">
                 <div class="bg-white p-6 rounded-xl shadow-lg w-80 flex-shrink-0">
                   <div class="flex items-center mb-4">
                     <img src="https://randomuser.me/api/portraits/men/7.jpg" class="w-12 h-12 rounded-full mr-4 border-2 border-indigo-100" alt="User Rahul"/>
                     <div>
                       <h4 class="text-lg font-semibold text-gray-900">Rahul Sharma</h4>
                       <div class="flex items-center text-yellow-500">
                          <i class="fa-solid fa-star text-sm"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star-half-stroke text-sm ml-0.5"></i>
                          <span class="text-xs text-gray-500 ml-2">(4.8)</span>
                       </div>
                     </div>
                   </div>
                   <p class="text-gray-600 text-sm leading-relaxed">"Karzo makes my daily commute incredibly easy. Booking is instant, and the multi-stop feature is a lifesaver for errands!"</p>
                 </div>
  
                 <div class="bg-white p-6 rounded-xl shadow-lg w-80 flex-shrink-0">
                   <div class="flex items-center mb-4">
                     <img src="https://randomuser.me/api/portraits/women/8.jpg" class="w-12 h-12 rounded-full mr-4 border-2 border-indigo-100" alt="User Ananya"/>
                     <div>
                       <h4 class="text-lg font-semibold text-gray-900">Ananya Verma</h4>
                        <div class="flex items-center text-yellow-500">
                          <i class="fa-solid fa-star text-sm"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <span class="text-xs text-gray-500 ml-2">(5.0)</span>
                       </div>
                     </div>
                   </div>
                   <p class="text-gray-600 text-sm leading-relaxed">"As a female rider, safety is paramount. I appreciate the driver verification and the safety gear reminders. Always feel secure with Karzo."</p>
                 </div>
  
                  <div class="bg-white p-6 rounded-xl shadow-lg w-80 flex-shrink-0">
                   <div class="flex items-center mb-4">
                     <img src="https://randomuser.me/api/portraits/men/9.jpg" class="w-12 h-12 rounded-full mr-4 border-2 border-indigo-100" alt="User Vikram"/>
                     <div>
                       <h4 class="text-lg font-semibold text-gray-900">Vikram Patel</h4>
                       <div class="flex items-center text-yellow-500">
                          <i class="fa-solid fa-star text-sm"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star-half-stroke text-sm ml-0.5"></i>
                          <span class="text-xs text-gray-500 ml-2">(4.7)</span>
                       </div>
                     </div>
                   </div>
                   <p class="text-gray-600 text-sm leading-relaxed">"Driving with Karzo gives me the flexibility I need. The app is intuitive, and the support team is responsive. Great way to earn."</p>
                 </div>
  
                  <div class="bg-white p-6 rounded-xl shadow-lg w-80 flex-shrink-0">
                   <div class="flex items-center mb-4">
                     <img src="https://randomuser.me/api/portraits/women/10.jpg" class="w-12 h-12 rounded-full mr-4 border-2 border-indigo-100" alt="User Meera"/>
                     <div>
                       <h4 class="text-lg font-semibold text-gray-900">Meera Nair</h4>
                       <div class="flex items-center text-yellow-500">
                          <i class="fa-solid fa-star text-sm"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <i class="fa-solid fa-star text-sm ml-0.5"></i>
                          <span class="text-xs text-gray-500 ml-2">(4.9)</span>
                       </div>
                     </div>
                   </div>
                   <p class="text-gray-600 text-sm leading-relaxed">"Booking event rides used to be stressful. Karzo's pre-booking option for events is fantastic. Reliable and always on time."</p>
                 </div>
               </template>
             </div>
          </div>
        </div>
      </section>
  
      <section class="py-16 md:py-24 bg-white" id="blogs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
           <div class="text-center mb-12">
             <h2 class="text-base font-semibold text-indigo-600 tracking-wide uppercase">Insights</h2>
             <p class="mt-2 text-3xl lg:text-4xl font-extrabold text-gray-900 tracking-tight">From the Karzo Blog</p>
             <p class="mt-4 max-w-2xl text-lg text-gray-500 mx-auto">
               Stay updated on ridesharing trends, safety tips, and company news.
             </p>
          </div>
  
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              <div class="flex flex-col bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
                  <img src="https://placehold.co/400x250/e0e7ff/4338ca?text=Blog+1&font=raleway" alt="Future of Ridesharing" class="w-full h-48 object-cover">
                  <div class="p-6 flex flex-col flex-grow">
                      <p class="text-sm font-semibold text-indigo-600">Industry Trends</p>
                      <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200 flex-grow">The Future of Urban Mobility: AI & Electric Rides</h3>
                      <p class="text-sm text-gray-600 mb-4 line-clamp-3">Explore how AI optimization and the shift to electric vehicles are revolutionizing the ridesharing experience for passengers and drivers alike.</p>
                      <div class="flex items-center text-xs text-gray-500 mt-auto pt-4 border-t border-gray-200">
                         <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Author" class="w-6 h-6 rounded-full mr-2">
                         <span>John Doe</span>
                         <span class="mx-1">|</span>
                         <span>March 10, 2025</span>
                         <span class="ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                            3 min read
                         </span>
                      </div>
                  </div>
              </div>
  
              <div class="flex flex-col bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
                  <img src="https://placehold.co/400x250/c7d2fe/4f46e5?text=Blog+2&font=raleway" alt="Smart City Transport" class="w-full h-48 object-cover">
                  <div class="p-6 flex flex-col flex-grow">
                      <p class="text-sm font-semibold text-indigo-600">Technology</p>
                      <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200 flex-grow">Integrating Karzo with Smart City Transportation</h3>
                      <p class="text-sm text-gray-600 mb-4 line-clamp-3">Learn how ridesharing platforms like Karzo are becoming integral parts of intelligent transportation systems, reducing congestion and promoting sustainability.</p>
                       <div class="flex items-center text-xs text-gray-500 mt-auto pt-4 border-t border-gray-200">
                         <img src="https://randomuser.me/api/portraits/women/33.jpg" alt="Author" class="w-6 h-6 rounded-full mr-2">
                         <span>Jane Smith</span>
                          <span class="mx-1">|</span>
                         <span>March 8, 2025</span>
                         <span class="ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                            4 min read
                         </span>
                      </div>
                  </div>
              </div>
  
               <div class="flex flex-col bg-gray-50 rounded-xl shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl group">
                  <img src="https://placehold.co/400x250/a5b4fc/5b21b6?text=Blog+3&font=raleway" alt="Driver Safety" class="w-full h-48 object-cover">
                  <div class="p-6 flex flex-col flex-grow">
                      <p class="text-sm font-semibold text-indigo-600">Driver Resources</p>
                      <h3 class="text-xl font-bold text-gray-900 mt-2 mb-3 group-hover:text-indigo-700 transition duration-200 flex-grow">Top 5 Safety Tips for Karzo Drivers</h3>
                      <p class="text-sm text-gray-600 mb-4 line-clamp-3">Your safety is our priority. Review these essential tips for staying safe and secure while driving on the Karzo platform.</p>
                      <div class="flex items-center text-xs text-gray-500 mt-auto pt-4 border-t border-gray-200">
                         <img src="https://randomuser.me/api/portraits/men/34.jpg" alt="Author" class="w-6 h-6 rounded-full mr-2">
                         <span>Alex Brown</span>
                          <span class="mx-1">|</span>
                         <span>March 5, 2025</span>
                         <span class="ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                            2 min read
                         </span>
                      </div>
                  </div>
              </div>
               </div>
           <div class="text-center mt-12">
              <button class="px-6 py-3 bg-indigo-600 text-white font-semibold rounded-md shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-200 ease-in-out">
                Visit Our Blog
              </button>
          </div>
        </div>
      </section>
  
      <footer class="bg-gray-900 text-gray-400 py-12 md:py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8 mb-8">
            <div class="col-span-2 lg:col-span-1">
               <div class="flex items-center gap-3 mb-4">
                  <img
                    src="https://placehold.co/40x40/ffffff/6366f1?text=K&font=raleway"
                    alt="Karzo Logo"
                    class="h-8 w-8 rounded-md"
                   />
                  <span class="text-xl font-bold text-white">Karzo</span>
               </div>
               <p class="text-sm mb-4">Connecting riders and drivers seamlessly.</p>
               <div class="flex space-x-4">
                  <a href="#" class="hover:text-white transition duration-200"><i class="fab fa-twitter fa-lg"></i></a>
                  <a href="#" class="hover:text-white transition duration-200"><i class="fab fa-facebook-f fa-lg"></i></a>
                  <a href="#" class="hover:text-white transition duration-200"><i class="fab fa-linkedin-in fa-lg"></i></a>
                  <a href="#" class="hover:text-white transition duration-200"><i class="fab fa-instagram fa-lg"></i></a>
               </div>
            </div>
  
            <div>
              <h3 class="text-sm font-semibold text-gray-300 tracking-wider uppercase mb-4">Company</h3>
              <ul class="space-y-2">
                <li><a href="#about" class="hover:text-white transition duration-200 text-sm">About Us</a></li>
                <li><a href="#careers" class="hover:text-white transition duration-200 text-sm">Careers</a></li>
                <li><a href="#blogs" class="hover:text-white transition duration-200 text-sm">Blog</a></li>
                <li><a href="#press" class="hover:text-white transition duration-200 text-sm">Press</a></li>
              </ul>
            </div>
  
            <div>
              <h3 class="text-sm font-semibold text-gray-300 tracking-wider uppercase mb-4">Product</h3>
              <ul class="space-y-2">
                <li><a href="#ride" class="hover:text-white transition duration-200 text-sm">Ride</a></li>
                <li><a href="#drive" class="hover:text-white transition duration-200 text-sm">Drive</a></li>
                <li><a href="#safety" class="hover:text-white transition duration-200 text-sm">Safety</a></li>
                <li><a href="#events" class="hover:text-white transition duration-200 text-sm">Events</a></li>
              </ul>
            </div>
  
            <div>
              <h3 class="text-sm font-semibold text-gray-300 tracking-wider uppercase mb-4">Resources</h3>
              <ul class="space-y-2">
                <li><a href="#help" class="hover:text-white transition duration-200 text-sm">Help Center</a></li>
                <li><a href="#cities" class="hover:text-white transition duration-200 text-sm">Cities</a></li>
                <li><a href="#fare-estimate" class="hover:text-white transition duration-200 text-sm">Fare Estimator</a></li>
              </ul>
            </div>
  
             <div>
              <h3 class="text-sm font-semibold text-gray-300 tracking-wider uppercase mb-4">Legal</h3>
              <ul class="space-y-2">
                <li><a href="#privacy" class="hover:text-white transition duration-200 text-sm">Privacy Policy</a></li>
                <li><a href="#terms" class="hover:text-white transition duration-200 text-sm">Terms & Conditions</a></li>
                <li><a href="#accessibility" class="hover:text-white transition duration-200 text-sm">Accessibility</a></li>
              </ul>
            </div>
  
          </div>
  
          <div class="border-t border-gray-700 pt-8 text-center text-sm">
            &copy; {{ new Date().getFullYear() }} Karzo Technologies Inc. All rights reserved. Website by Yash Patkar.
          </div>
        </div>
      </footer>
  
    </div>
  </template>
  
<style>
@keyframes scroll {
    from {
        transform: translateX(0);
    }

    to {
        transform: translateX(-50%);
    }
}

.animate-scroll {
    display: flex;
    width: max-content;
    animation: scroll 15s linear infinite;
}

.line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>