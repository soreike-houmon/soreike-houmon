// それいけ！訪問マッサージはり・きゅう 共通スクリプト

// スマホのメニュー開閉
(function () {
  var btn = document.querySelector('.menu-toggle');
  var nav = document.getElementById('global-nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    btn.textContent = open ? 'メニュー' : '閉じる';
    nav.classList.toggle('is-open', !open);
  });
})();

// お問い合わせフォーム
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;

  // 採用情報ページから来たとき（contact.html?type=recruit）は「求人応募・相談」を選んだ状態にする
  var type = new URLSearchParams(location.search).get('type');
  var select = document.getElementById('f-type');
  if (type && select) {
    var option = select.querySelector('option[data-key="' + type + '"]');
    if (option) option.selected = true;
  }

  // 送信：Formspree へ裏側で送り、成功したら送信完了ページ（thanks.html）へ移動する
  var button = document.getElementById('form-submit-btn');
  var errorBox = document.getElementById('form-error');
  var buttonLabel = button ? button.textContent : '';
  var sending = false;

  function resetButton() {
    sending = false;
    if (button) {
      button.disabled = false;
      button.textContent = buttonLabel;
    }
  }

  form.addEventListener('submit', function (e) {
    // fetch が使えない古いブラウザでは、通常の送信（Formspree の画面に移動）に任せる
    if (!window.fetch || !window.FormData) return;

    e.preventDefault();
    if (sending) return; // 二重送信を防ぐ
    sending = true;
    if (errorBox) errorBox.hidden = true;
    if (button) {
      button.disabled = true;
      button.textContent = '送信しています…';
    }

    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    })
      .then(function (res) {
        if (res.ok) {
          location.href = 'thanks.html';
          return;
        }
        return res.json().catch(function () { return {}; }).then(function (data) {
          var text = JSON.stringify(data || {}).toLowerCase();
          if (text.indexOf('captcha') !== -1) {
            // 迷惑メール対策の確認（reCAPTCHA）が必要なときは、通常の送信に切り替える
            form.submit();
            return;
          }
          throw new Error('send failed');
        });
      })
      .catch(function () {
        resetButton();
        if (errorBox) errorBox.hidden = false;
      });
  });
})();
