function ghostCursor(options) {
  let hasWrapperEl = options && options.element
  let element = hasWrapperEl || document.body

  let width = window.innerWidth
  let height = window.innerHeight
  let cursor = { x: width / 2, y: width / 2 }
  let particles = []
  let canvas, context

  let baseImage = new Image()
  baseImage.src =
    "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAB0AAAAfCAQAAACxUg6PAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAAAMgAAADIAGP6560AAAAHdElNRQflBxwDLzFjNpKoAAAAAW9yTlQBz6J3mgAAABBjYU52AAAAIAAAACAAAAAAAAAAAGK57voAAAI5SURBVDjLzZXfS1NhGMdfV1BIQpirlW2gMxdrST80NguPrlTMtumcy010ZVu4Sm1ttQRrkrrqEIP6HyTyT+gq6iLQu66LMOouKgoCM/v2nRSkO+9qu+p5OXA4Dx+e7/N9n/c9onZ076XqclFMmGMWmJbK5kSH2FAgWtluQClEdt0rEN1sXMV+iHFRUqjiEvFFfBauoroVs8Iqigyd+A9Ddc54JwYSvqilICxVpirqo/T8jdexhfDMWfs/g5ludfkhMriFqxhDDNcx+HKw96/YZPnt4B2kCPWhE618TiPMFXre62vKb+zdofST+4hAQTUqoEcNjhG+jH50vVGq8qLTyw8wgHpim7AVlTDiINoQxDmMwH7GJKubNEz5Ux/jcKxszw7pr7ChBd3oQResz8wJCRq33HwaXwpQain+/H4KbSseOCne8FiCXnFMYfi7AgO2rEEjcMGNo3Bg2wcJmnBm2GcddmJ9JkCrmtAA/VsJetGlsisLategXvoaoufH6br+nQwNpuHFPhzJqTr0aYw2tcirRtxZ1AZ7DjqMBD3Og4Zb0zRkPxpz0Au4RqOccjTaPI2TFGwvHPUrk0StGlWjnGlfPsF9ygR9tHEHtVA3TsCwKEWTFGXVQM9zgj1ohnFROvxJiqrREBzisev41ojdLyRgPwI4zJFw5aA8r9ztPZyzA9BER9npIexCxav1mfbZhvf1zJjYsSY6wjuhEzu+auWqzH5WrOPdoZEc1/yB6Db+fvOsHvMe3U/2gSuHKOmTLAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMS0wNy0yOFQwMzo0Nzo0OSswMDowMAi4ye0AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjEtMDctMjhUMDM6NDc6NDgrMDA6MDDfknrlAAAAAElFTkSuQmCC"

  function init() {
    canvas = document.createElement("canvas")
    context = canvas.getContext("2d")
    canvas.style.top = "0px"
    canvas.style.left = "0px"
    canvas.style.pointerEvents = "none"

    if (hasWrapperEl) {
      canvas.style.position = "absolute"
      element.appendChild(canvas)
      canvas.width = element.clientWidth
      canvas.height = element.clientHeight
    } else {
      canvas.style.position = "fixed"
      document.body.appendChild(canvas)
      canvas.width = width
      canvas.height = height
    }

    bindEvents()
    loop()
  }

  // Bind events that are needed
  function bindEvents() {
    element.addEventListener("mousemove", onMouseMove)
    element.addEventListener("touchmove", onTouchMove)
    element.addEventListener("touchstart", onTouchMove)
    window.addEventListener("resize", onWindowResize)
  }

  function onWindowResize(e) {
    width = window.innerWidth
    height = window.innerHeight

    if (hasWrapperEl) {
      canvas.width = element.clientWidth
      canvas.height = element.clientHeight
    } else {
      canvas.width = width
      canvas.height = height
    }
  }

  function onTouchMove(e) {
    if (e.touches.length > 0) {
      for (let i = 0; i < e.touches.length; i++) {
        addParticle(e.touches[i].clientX, e.touches[i].clientY, baseImage)
      }
    }
  }

  function onMouseMove(e) {
    if (hasWrapperEl) {
      const boundingRect = element.getBoundingClientRect()
      cursor.x = e.clientX - boundingRect.left
      cursor.y = e.clientY - boundingRect.top
    } else {
      cursor.x = e.clientX
      cursor.y = e.clientY
    }

    addParticle(cursor.x, cursor.y, baseImage)
  }

  function addParticle(x, y, image) {
    particles.push(new Particle(x, y, image))
  }

  function updateParticles() {
    context.clearRect(0, 0, width, height)

    // Update
    for (let i = 0; i < particles.length; i++) {
      particles[i].update(context)
    }

    // Remove dead particles
    for (let i = particles.length - 1; i >= 0; i--) {
      if (particles[i].lifeSpan < 0) {
        particles.splice(i, 1)
      }
    }
  }

  function loop() {
    updateParticles()
    requestAnimationFrame(loop)
  }

  /**
   * Particles
   */

  function Particle(x, y, image) {
    const lifeSpan = 40
    this.initialLifeSpan = lifeSpan //ms
    this.lifeSpan = lifeSpan //ms
    this.position = { x: x, y: y }

    this.image = image

    this.update = function(context) {
      this.lifeSpan--
      const opacity = Math.max(this.lifeSpan / this.initialLifeSpan, 0)

      context.globalAlpha = opacity
      context.drawImage(
        this.image,
        this.position.x, // - (this.canv.width / 2) * scale,
        this.position.y //- this.canv.height / 2,
      )
    }
  }

  init()
}
