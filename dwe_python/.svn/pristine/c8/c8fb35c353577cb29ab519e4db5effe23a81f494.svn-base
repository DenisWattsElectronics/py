clear all
clc
format shortE;
tic
% 
% % % Программа для проверки методики расчета BER для диссертации
% % % Версия: 0.1 030919
% % % Автор: Доможаков Д.А. 
% 

UI = 320e-12;           % Длина битового интервала
n_UI = 10000000;              % Длинна выборки
j_det_total = 0e-12;    % Суммарный детерминированный джиттер
j_random_total = 50e-12; % Суммарный случайный джиттер
Th_01 = 0e-12;          % Времена Setup и Hold десериализатора по потоку данных
Th_10 = 0e-12;
Ts_10 = 0e-12;
Ts_01 = 0e-12;
threshold = UI/2;
N = 1;

bits = zeros(n_UI,N);       
correctly_exp = zeros(N,1);
fail_exp = zeros(N,1);
BER_exp = zeros(N,1);

%  Передаваемый код:
% bits = [0 1 0 1 0 0 1 1 0 0 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1];
bits = [ 0 1 0 0 1 1 0 0 0 1 1 1 0 0 0 0 1 1 1 1 ];
% bits = [0 0 1 1];
cross = zeros(n_UI,1); %  Cross массив
cross_clear = zeros(n_UI,1); % Cross без шума
cross_direction = zeros(n_UI,1); % Направление перепада (не используется)


% Построение чистого cross для передаваемого сигнала
bit_pointer = 2; % Указатель внутри массива bits
prev_bit = true; % Предыдущий бит для формирования или игнорирования перепада
if bits(1,1) == 0  
    prev_bit = false;
elseif bits(1,1) == 0
    prev_bit = true;
end
add_UI = 0e-12; % Приращение функции cross. Зависит от уровня предыдущего перепада

cross_pointer = 2; % Указатель массива cross
cross_check_add = zeros(length(cross),1); % Массив с приращениями для проверки алгоритма построения cross

%  Создание чистого cross
for i = 2:n_UI
    if bit_pointer > length(bits)
        bit_pointer = 2;
    end    
    if (bits(1,bit_pointer) == bits(1, bit_pointer-1))
        add_UI = add_UI + UI;                 
    else
        cross(cross_pointer,1) = cross(cross_pointer-1,1) + add_UI;  
        cross_pointer = cross_pointer + 1;
        cross_check_add(cross_pointer,1) = add_UI;
        add_UI = UI;
    end
    bit_pointer = bit_pointer + 1;
end
cross = cross(3:cross_pointer-1);


% % Создание проверки для cross
% cross = cross(1:cross_pointer-1);
% cross_pointer;
% cross_check_add = cross_check_add(1:cross_pointer-1);
% size(cross_check_add);
% % plot(cross_check_add);

% Зашумление cross
cross_clear = cross;
for i = 1:length(cross)
   cross(i,1) = cross(i,1) + normrnd(0,j_random_total);
end


% Создание проверки для cross
cross_pointer;
cross_check_add = cross_check_add(1:cross_pointer-1);
size(cross_check_add);
cross_check_add;
% plot(cross_check_add);

% Подсчет числа эмпирических ошибок 
jitter = cross - cross_clear; % Массив с джиттером

fail_exp = 0;
correctly_exp = 0;
all_exp = 0;


% for k = 1:N
for i = 1:length(jitter)
    if jitter(i,1) >= threshold
        fail_exp = fail_exp + 1;
    else 
        correctly_exp = correctly_exp + 1;
    end
    all_exp = all_exp + 1;
end

fail_exp
correctly_exp


BER_exp_invartiant = fail_exp/all_exp
BER_exp_code = fail_exp/n_UI

n_UI
all_exp

pd = makedist( 'Normal', 'mu', 0, 'sigma', j_random_total );
BER_distr_invariant = 1 - ( cdf( pd, threshold ) )
BER_distr_code = BER_distr_invariant*all_exp/n_UI





timeElapsed = toc