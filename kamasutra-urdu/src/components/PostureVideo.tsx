import { useRef, useState } from 'react';

import { getAssetUrl } from '../utils/assets';

interface PostureVideoProps {
  src: string;
  poster?: string;
  title: string;
  captionUrdu?: string;
}

export function PostureVideo({ src, poster, title, captionUrdu }: PostureVideoProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [playing, setPlaying] = useState(false);
  const [muted, setMuted] = useState(true);
  const [error, setError] = useState(false);

  const resolvedSrc = getAssetUrl(src);
  const resolvedPoster = poster ? getAssetUrl(poster) : undefined;

  const togglePlay = () => {
    const video = videoRef.current;
    if (!video) return;
    if (video.paused) {
      void video.play();
      setPlaying(true);
    } else {
      video.pause();
      setPlaying(false);
    }
  };

  const toggleMute = () => {
    const video = videoRef.current;
    if (!video) return;
    video.muted = !video.muted;
    setMuted(video.muted);
  };

  return (
    <div className="posture-video">
      <div className="video-wrapper">
        <video
          ref={videoRef}
          src={resolvedSrc}
          poster={resolvedPoster}
          loop
          playsInline
          muted={muted}
          preload="auto"
          onPlay={() => setPlaying(true)}
          onPause={() => setPlaying(false)}
          onError={() => setError(true)}
          onClick={togglePlay}
          aria-label={title}
        />
        <div className="video-overlay">
          {!playing && (
            <button
              className="video-play-btn"
              onClick={togglePlay}
              type="button"
              aria-label="چلائیں"
            >
              ▶
            </button>
          )}
          <button
            className="video-mute-btn"
            onClick={toggleMute}
            type="button"
            aria-label={muted ? 'آواز آن' : 'آواز بند'}
          >
            {muted ? '🔇' : '🔊'}
          </button>
        </div>
      </div>
      {error && <p className="video-error">ویڈیو لوڈ نہیں ہوئی — دوبارہ کوشش کریں</p>}
      {captionUrdu && <p className="video-caption">{captionUrdu}</p>}
    </div>
  );
}
